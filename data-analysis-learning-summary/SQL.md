# 数据分析常用SQL语句练习

## 环境
系统：macOS 10.12
数据库：mysql5.7.2
GUI:Sequel Pro1.1
数据来源：秦路的公众号，[数据在这里](https://github.com/hujieying/Data-Analysis/blob/master/data-analysis-learning-summary/DataAnalyst.csv)

## 数据
本次练习数据是直接使用秦路文章中使用的现成的数据作为练习。数据是用爬虫爬取招聘网站上约5000条的数据分析师职位数据。为了练习，数据中北京数据多复制了一份。
具体数据包括字段：
> city：城市
companyFullName：公司全名
companyId：公司ID
companyLabelList：公司介绍标签
companyShortName：公司简称
companySize：公司大小
businessZones：公司所在商区
firstType：职位所属一级类目
secondType：职业所属二级类目
education：教育要求
industryField：公司所属领域
positionId：职位ID
positionAdvantage：职位福利
positionName：职位名称
positionLables：职位标签
salary：薪水
workYear：工作年限要求

在数据库中长这个样子：
![数据样子](https://raw.githubusercontent.com/hujieying/Data-Analysis/master/pic/a0.png)


## 从入门到熟练
* 我想看城市为深圳的职位数据：
> select * from data where city = '深圳'  

![a1.png (977×380)](https://raw.githubusercontent.com/hujieying/Data-Analysis/master/pic/a1.png)


* 我想看城市为深圳且职位名是数据分析师的数据：数据分析方向有好多叫法。
> select * from data where city = '深圳' and positionName = '数据分析师'

![a2.png (959×377)](https://raw.githubusercontent.com/hujieying/Data-Analysis/master/pic/a2.png)


* 我想看深圳的数据分析师或者北京的产品经理数据：看看不同城市不同名称的职位量。
> select * from data
where (city = '深圳' and positionName = '数据分析师') or (city = '北京' and positionName = '数据产品经理')

![a3.png (967×383)](https://raw.githubusercontent.com/hujieying/Data-Analysis/master/pic/a3.png)


* 我想看深圳成都北京上海这几个城市的数据：多看几个城市的职位数据。
>select * from data
where city in ('深圳','成都','北京','上海')

* 模糊查找，用like搭配%。
> select * from data where positionName like '%数据分析%'

![a5.png (974×377)](https://raw.githubusercontent.com/hujieying/Data-Analysis/master/pic/a5.png)


* 看看都有哪些城市有职位需求：
> select city from data group by city

![a6.png (280×363)](https://raw.githubusercontent.com/hujieying/Data-Analysis/master/pic/a6.png)


* 我想看每个城市的职位数量：使用count计算数量，除了count，还有max，min，sum，avg等，也叫聚合函数。通过distinct对职位ID进行去重，避免重复统计。实际使用中，活跃用户数、文章UV，都可用distinct计算。
> select city,count(distinct positionId) from data group by city

![a7.png (452×375)](https://raw.githubusercontent.com/hujieying/Data-Analysis/master/pic/a7.png)


* 用group by添加多个字段，将以多维形式进行数据聚合。
> select city,workYear,count(distinct positionId) from data group by city,workYear

![a8.png (600×379)](https://raw.githubusercontent.com/hujieying/Data-Analysis/master/pic/a8.png)


* 我想知道不同城市，电商领域岗位的职位有多少，占比是多少：使用count结合if计算电商的职位数，职位数最后除以城市职位总数就可以得出占比，所以这里需要求出分母和分子两个数。第一个count计算职位总数。第二个count计算电商职位数，if函数中间字段代表为true时返回的值，为避免重复数据，这里根据数据源的特征使用唯一标识positionId来进行计数；if第三个参数写成null是为避免count对其计数。
> select city,count(distinct positionId),count(if(industryField like '%电子商务%',positionId,null)) from data
group by city

![a9.png (707×382)](https://raw.githubusercontent.com/hujieying/Data-Analysis/master/pic/a9.png)


* 我想知道各个城市数据分析师岗位数量在500以上的城市有哪些：
第一种：使用having对聚合后数据进行过滤
第二种：利用嵌套子查询，as表示命名
> select city,count(distinct positionId) from data
group by city having count(distinct positionId)>=500

![a10.png (413×210)](https://raw.githubusercontent.com/hujieying/Data-Analysis/master/pic/a10.png)


> select * from(select city,count(distinct positionId) as counts from data group by city) as t1
where counts >=500

* 使用order by让数据按顺序显示:降序在最后加desc
>select city,count(distinct positionId) as counts from data group by city
order by counts

![a11.png (490×381)](https://raw.githubusercontent.com/hujieying/Data-Analysis/master/pic/a11.png)


* 我想得到每个岗位工资最高和最低，原始数据是在salary字段里面，这里做一个数据清洗：  
locate函数查找第一个k所在位置，left函数获取k前面位置的数字，得到下限；  
substr函数第二个参数表示从哪里开始截取，第三个参数表示截取长度；locate函数查找-的位置+1表示横杠后面的位置作为第二个参数，length函数减去locate函数表示第三个参数。
> select left(salary,locate('k',salary)-1) as bottomSalary,
substr(salary,locate('-',salary)+1,length(salary)-locate('-',salary)-1) as topSalary,
salary from data
where salary not like '%以上%'

![a12.png (661×296)](https://raw.githubusercontent.com/hujieying/Data-Analysis/master/pic/a12.png)


* 我想得到不同城市不同工作年限的平均薪资，当然这里薪资是一个范围，不能表示真实情况，仅作为练习。
> select city,workYear,avg((bottomSalary+topSalary)/2) as avgSalary from(
select left(salary,locate('K',salary)-1) as bottomSalary,
substr(salary,locate('-',salary)+1,length(salary)-locate('-',salary)-1) as topSalary,
city,positionId,workYear
from data
where salary not like '%以上%') as t1
group by city,workYear
order by city,avgSalary

![a13.png (636×380)](https://raw.githubusercontent.com/hujieying/Data-Analysis/master/pic/a13.png)

## 从熟练到掌握
到leetcode.com上刷题。
