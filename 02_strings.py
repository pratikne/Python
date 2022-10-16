story = "once upon a time ...Ram was ruling Ayodhya"
print(len(story)); #returns length
print(story.endswith("...")) #True..returns bool
print(story.count("a")) #1
print(story.count("upon")) #1
print(story.capitalize()) #returns string with 1st letter capatilized
print(story.find("upon")) #returns index where upon starts(1st occurence) i.e 5
#if -1 s returned...string isnt found
story = story.replace("Ram","Bharat")
print(story.replace("Ram","Bharat")) 


ita=iter(story)
print(next(ita))