dict = eval(input())
    
income = float(input())

def func(dict, income):


    income_level = dict["INCOME"]
    marital_status = dict["MARITAL_STATUS"]
    child = dict["CHILD"]
    special_needs = dict["SPECIAL_NEEDS"]
    elderly_care = dict["ELDERLY_CARE"]
    taxpayer_duration = dict["TAXPAYER_DURATION"]
    city_category = dict["CITY_CATEGORY"]
    education = dict["EDUCATION"]
    healthcare = dict["HEALTHCARE"]
    green_initiatives = dict["GREEN_INITIATIVES"]
    property_status = dict["PROPERTY_STATUS"]

    base_tax_rates = {"low": (0.10), "middle": (0.20), "high": (0.30)}
    base_tax = income * base_tax_rates[income_level]
    
    if marital_status == "single":
        base_tax = base_tax
    elif marital_status == "married":
        base_tax -= 500
        base_tax -= (300 * len(child))
    elif marital_status == "single_parent":
        base_tax -= (600 * len(child))

  
    
    def dependent_child(child, base_tax):
        if child == []:
            return base_tax
        
        child_age = child[0]
        if child_age < 18:
            base_tax -= 200
        return dependent_child(child[1:], base_tax)
    
    base_tax = dependent_child(child, base_tax)



    if special_needs == True:
        base_tax -= 1000


    
    if elderly_care == True:
        base_tax -= 800



    if city_category == "urban":
        base_tax = base_tax         #return base_tax
    elif city_category == "suburban":
        base_tax -= 200
    elif city_category == "rural":
        base_tax -= 400

    
    if education == True:
        base_tax -= 500


    
    if healthcare == True:
        base_tax -= 750


    
    if green_initiatives == True:
        base_tax -= 300


    
    if property_status == "owns":
        base_tax = base_tax
    elif property_status == "rents":
        base_tax -= 300


    
    if taxpayer_duration == "new":
        base_tax = base_tax
    elif taxpayer_duration ==  "regular":
        base_tax = base_tax * (0.95)
    elif taxpayer_duration == "long_term":
        base_tax = base_tax * (0.90)

    

    if base_tax < 0:
        base_tax = 0
        
    return base_tax


final_tax_amount = func(dict, income)
print("%.2f" % final_tax_amount)




    
