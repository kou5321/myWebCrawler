from lxml import etree

text='''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
     </ul>
 </div>
'''

html=etree.HTML(text,etree.HTMLParser())
result=html.xpath('//li[@class="item-1"]/a/text()') #获取a节点下的内容
result1=html.xpath('//li[@class="item-1"]//text()') #获取li下所有子孙节点的内容

print(result)
print(result1)