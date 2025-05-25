
# chnage item value 
# To change the value of a specific item refer to the index number

thilist=["apple","banana",'cherry']
thilist[1] ="blackurreant"
print(thilist)

# change a range of item values

thilist =['apple','banana','cherry',"orange",'kiwi','mango']
thilist[1:3]=["blackcurrunet","watermelon"]
print(thilist)

thilist=['apple','banana','cherry']
thilist[1:2]=["blackurrant",'watermelon']
print(thilist)

thilist=['apple',"banana","cherry"]
thilist[1:3]=['watermelon']
print(thilist)


# insert items

# To insert a new item  without replaceing any of the existting values we can use the insert method 

thilist =['apple','banana','cherry']
thilist.insert(2,'watermelon')
print(thilist)





