# 数据可视化
## 概念
维度：观察数据的角度和对数据的描述。比如地区、销售额。维度可以用时间、数值、文本表示。数据分析的本质是各种维度的组合。  
维度类型和转换：维度主要是三大类的数据结构：文本、时间、数值。维度可以互相转换。比如年龄原本是数值型的维度，但是可以通过对年龄的划分，将其分类为小孩、青年、老年三个年龄段，此时就转换为文本维度。  

## 常用可视化图表

![](http://mmbiz.qpic.cn/mmbiz_png/9WoCz1BTJSgqXoT3mVgw6Hibf6Gr6HOPYVzKRj1COU5I85SWCMhr17D0ngtskrPQcTxIGFZUcB9QPB36mdvPziaQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)

|序号|类型|作用|适用场景|适用数据|优点|缺点|图示|
|--------|:--------|:--------|:--------|:--------|:--------|:--------|--------|
|1|散点图scatter plot|揭示数据之间的关系，发觉变量与变量之间的关联|两个维度比较（地图某地区某项数据集中分布），对离散数据进行预测时|离散值数据|直观反映数据集中情况，对离散数据线性回归等曲线预测性的拟合辅助作用|适用场景较少|![](http://mmbiz.qpic.cn/mmbiz_png/9WoCz1BTJSiagccNuibiaIGcnfEsHyg9CYZhYGtK28icicqtALHTB8xwS9P7ibo0QeuVMn7b5A73lAkzTL5Tcwznn3zg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)|
|2|折线图line chart|想要了解某一维度在时间上的规律或者趋势时，折线图分为 直线折线图和曲线折线图，直线折线图适用于离散变量，曲线折线图适用于连续变量|需要反映变化趋势，关联性|时间序列类数据、关联类数据|直观反映数据变化趋势|数据集太小时显示不直观|![](http://mmbiz.qpic.cn/mmbiz_png/9WoCz1BTJSiagccNuibiaIGcnfEsHyg9CYZsLZMH2VyXiaYf0iarSB8ZqI3CdD7gte752zp89YEZ8k8cBIz4MwcJ3pA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)|
|3|柱形图bar chart|常用于多个维度的比较和变化|一个维度数据比较、数据单纯性展示、排序数据展示|数据集不大，二维数据|人眼对高度较敏感，直观各组数据差异性，强调个体与个体之间的比较|不适合大量的数据集数据（项数较多）|![](http://mmbiz.qpic.cn/mmbiz_png/9WoCz1BTJSiagccNuibiaIGcnfEsHyg9CYZSLicL8vJJaozSSkYsqme4aLeCJOt7XkAicEyPBWoo9V3k09tBhhhf7wA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)|
|4|地理图|一切和空间属性有关的分析都可以用到地理图。比如各地区销量，或者某商业区域店铺密集度等|||||![](http://mmbiz.qpic.cn/mmbiz_png/9WoCz1BTJSiagccNuibiaIGcnfEsHyg9CYZ8ticnfPmrTib01IZ0Sh0gCZbjeg4sB5dfias4riarDsdM8BPXUuP02iaChA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)|
|5|饼图pie|饼图经常表示一组数据的占比。可以用扇面、圆环、或者多圆环嵌套。商务类的汇报中应用较多。|一个维度各项指标（一般不超过5个项目）占总体的占比情况，分布情况。|具有整体意义的各项相同数据|直观显示各项占总体的占比，分布情况，强调整个与个体间的比较。|数据不精细，不适合分类较多的情况|![](http://mmbiz.qpic.cn/mmbiz_png/9WoCz1BTJSiagccNuibiaIGcnfEsHyg9CYZ26iaicbOlol9O3mdKJSzQ74JANxOquvmkgLu6mp7csXJ6npfmussAFfA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)|
|6|雷达图|也叫蛛网图。它在商务、财务领域应用较大，适合用在固定的框架内表达某种已知的结果。常见于经营状况，财务健康程度。|||||![](http://mmbiz.qpic.cn/mmbiz_png/9WoCz1BTJSiagccNuibiaIGcnfEsHyg9CYZF51mu57icMDZyq0UKdYkNJ6bF45q3Pibm5icVKRUbcRicPWLTso28fHrwA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)|
|7|箱线图|它能准确地反映数据维度的离散（最大数、最小数、中位数、四分数）情况。|假如你是一位互联网电商分析师，你想知道某商品每天的卖出情况：该商品被用户最多购买了几个，大部分用户购买了几个，用户最少购买了几个。箱线图就能很清晰的表示出上面的几个指标以及变化。|离散数据|||![](http://mmbiz.qpic.cn/mmbiz_png/9WoCz1BTJSiagccNuibiaIGcnfEsHyg9CYZT37GGvdwDNP3PdBY8Gmia7u5FDNKqULYE44SrvHU2VQbULFmYKxtbpQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)|
|8|热力图|以高亮形式展现数据|||||![](http://mmbiz.qpic.cn/mmbiz_png/9WoCz1BTJSiagccNuibiaIGcnfEsHyg9CYZ7XXX3Y7lOtCsRCt4UryQu5e8wvveIW7AkmPC0lZ4IticfUMcaaDBkibg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)|
|9|关系图|展现事物相关性和关联性的图表，比如社交关系链、品牌传播、或者某种信息的流动。依赖大量的数据，本身没有维度的概念|||||![](http://mmbiz.qpic.cn/mmbiz_png/9WoCz1BTJSiagccNuibiaIGcnfEsHyg9CYZwFuiaqbp7VvYhBoRvGYiaKl3cLIPW3Duv3CmgVgcANMncQl2horFBs6A/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)|
|10|矩形树图||电子商务、产品销售等涉及大量品类的分析||||![](http://mmbiz.qpic.cn/mmbiz_png/9WoCz1BTJSiagccNuibiaIGcnfEsHyg9CYZ85dtCjxGq62vM8xYCpunFAGec4ZB6JRC1OgNCJ1zL1lQcUUPfPSibEA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)|
|11|桑基图|常表示信息的变化和流动状态|||||![](http://mmbiz.qpic.cn/mmbiz_png/9WoCz1BTJSiagccNuibiaIGcnfEsHyg9CYZTr1coiczwPm46iadzYiaG3r8hFOTlSAR7GR1o1xvP9LU356pfwqyYTDjA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)|
|12|漏斗图|转化率可视化，它适用在固定流程的转化分析，你也可以认为它是桑基图的简化版|||||![](http://mmbiz.qpic.cn/mmbiz_png/9WoCz1BTJSiagccNuibiaIGcnfEsHyg9CYZg8IyF3lwcX6Bje3VibMdDPfARU1KG3DgIOYYgAp72U4UJP2CP9CicyYQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1)|

学习参考资料：  
[数据可视化：你想知道的经典图表全在这](https://mp.weixin.qq.com/s?__biz=MjM5NjEyMDI2MQ==&mid=2455946767&idx=1&sn=631135d8fe90b3b9c9e7983bf64fc77c&chksm=b17875a5860ffcb3e0b99adcfcfbf95df76d02e40c2e415d92478712b3590ae1c729146fdcfc&scene=21#wechat_redirect)  
[数据可视化：常用图表使用总结](http://www.woshipm.com/data-analysis/779858.html)  
[数据可视化：常用图表类型](http://www.afenxi.com/post/16416)


## CHANGELOG  
20180102 增补  
20171231 创建
