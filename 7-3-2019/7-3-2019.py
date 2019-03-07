inventory={
            "gold":500,
            "pound":["flint","gemstore","twine"],
            "backpack":["xyclophone","dagger","bedroll","break loaf"],
          
}
inventory["pocket"]=["seashell","strange bery","lint"]
# print(inventory,sep=",")
# a=list(inventory)
inventory["backpack"].remove("dagger")
inventory["gold"]=inventory["gold"]+50
print(inventory)

