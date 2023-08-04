from lxml import etree

xml = """
<ul id="select-list" class="select-list" tabindex="-1" role="listbox" style="bottom: 43px; border-bottom: 0px; border-top-left-radius: 6px; border-top-right-radius: 6px; width: 190.656px;"><li id="list-option0" role="option" class="select-option is-selected" tabindex="-1">Choose</li><li id="list-option1" role="option" class="select-option" tabindex="-1">Alabama</li><li id="list-option2" role="option" class="select-option" tabindex="-1">Alaska</li><li id="list-option3" role="option" class="select-option" tabindex="-1">American Samoa</li><li id="list-option4" role="option" class="select-option" tabindex="-1">Arizona</li><li id="list-option5" role="option" class="select-option" tabindex="-1">Arkansas</li><li id="list-option6" role="option" class="select-option" tabindex="-1">California</li><li id="list-option7" role="option" class="select-option" tabindex="-1">Colorado</li><li id="list-option8" role="option" class="select-option" tabindex="-1">Connecticut</li><li id="list-option9" role="option" class="select-option" tabindex="-1">Delaware</li><li id="list-option10" role="option" class="select-option" tabindex="-1">Florida</li><li id="list-option11" role="option" class="select-option" tabindex="-1">Georgia</li><li id="list-option12" role="option" class="select-option" tabindex="-1">Guam</li><li id="list-option13" role="option" class="select-option" tabindex="-1">Hawaii</li><li id="list-option14" role="option" class="select-option" tabindex="-1">Idaho</li><li id="list-option15" role="option" class="select-option" tabindex="-1">Illinois</li><li id="list-option16" role="option" class="select-option" tabindex="-1">Indiana</li><li id="list-option17" role="option" class="select-option" tabindex="-1">Iowa</li><li id="list-option18" role="option" class="select-option" tabindex="-1">Kansas</li><li id="list-option19" role="option" class="select-option" tabindex="-1">Kentucky</li><li id="list-option20" role="option" class="select-option" tabindex="-1">Louisiana</li><li id="list-option21" role="option" class="select-option" tabindex="-1">Maine</li><li id="list-option22" role="option" class="select-option" tabindex="-1">Maryland</li><li id="list-option23" role="option" class="select-option" tabindex="-1">Massachusetts</li><li id="list-option24" role="option" class="select-option" tabindex="-1">Michigan</li><li id="list-option25" role="option" class="select-option" tabindex="-1">Minnesota</li><li id="list-option26" role="option" class="select-option" tabindex="-1">Mississippi</li><li id="list-option27" role="option" class="select-option" tabindex="-1">Missouri</li><li id="list-option28" role="option" class="select-option" tabindex="-1">Montana</li><li id="list-option29" role="option" class="select-option" tabindex="-1">Nebraska</li><li id="list-option30" role="option" class="select-option" tabindex="-1">Nevada</li><li id="list-option31" role="option" class="select-option" tabindex="-1">New Hampshire</li><li id="list-option32" role="option" class="select-option" tabindex="-1">New Jersey</li><li id="list-option33" role="option" class="select-option" tabindex="-1">New Mexico</li><li id="list-option34" role="option" class="select-option" tabindex="-1">New York</li><li id="list-option35" role="option" class="select-option" tabindex="-1">North Carolina</li><li id="list-option36" role="option" class="select-option" tabindex="-1">North Dakota</li><li id="list-option37" role="option" class="select-option" tabindex="-1">Northern Marianas</li><li id="list-option38" role="option" class="select-option" tabindex="-1">Ohio</li><li id="list-option39" role="option" class="select-option" tabindex="-1">Oklahoma</li><li id="list-option40" role="option" class="select-option" tabindex="-1">Oregon</li><li id="list-option41" role="option" class="select-option" tabindex="-1">Pennsylvania</li><li id="list-option42" role="option" class="select-option" tabindex="-1">Puerto Rico</li><li id="list-option43" role="option" class="select-option" tabindex="-1">Rhode Island</li><li id="list-option44" role="option" class="select-option" tabindex="-1">South Carolina</li><li id="list-option45" role="option" class="select-option" tabindex="-1">South Dakota</li><li id="list-option46" role="option" class="select-option" tabindex="-1">Tennessee</li><li id="list-option47" role="option" class="select-option" tabindex="-1">Texas</li><li id="list-option48" role="option" class="select-option" tabindex="-1">Utah</li><li id="list-option49" role="option" class="select-option" tabindex="-1">Vermont</li><li id="list-option50" role="option" class="select-option" tabindex="-1">Virginia</li><li id="list-option51" role="option" class="select-option" tabindex="-1">Virgin Islands(US)</li><li id="list-option52" role="option" class="select-option" tabindex="-1">Washington</li><li id="list-option53" role="option" class="select-option" tabindex="-1">Washington DC</li><li id="list-option54" role="option" class="select-option" tabindex="-1">West Virginia</li><li id="list-option55" role="option" class="select-option" tabindex="-1">Wisconsin</li><li id="list-option56" role="option" class="select-option" tabindex="-1">Wyoming</li></ul>
"""

ele = etree.HTML(xml)
result = ele.xpath("//li/text()")
print(result)
result = ['Choose', 'Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Marianas', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Virgin Islands(US)', 'Washington', 'Washington DC', 'West Virginia', 'Wisconsin', 'Wyoming']
print(result.index("Alaska"))