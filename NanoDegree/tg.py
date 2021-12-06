bio = """**Friends Don't swipe right if you think make up is fake or beauty is defined by any color, size and shape.
Otherwise:
**fat foodie**
**Makeup Junkie**
**Always happy**
**Gemini**
**procrastinator**
**Singer (at times)**
**Dancer (at times)**
**Play Ukulele (occasionally)**
**hate to show off**
**📸 Insta: Sharnya_malhotra**
**Friends Fan**
***Isn't that just kick you in the crotch,, spit on your neck fantastic**
# True Sharnya_malhotra**
# **Friends Don't swipe right if you think make up is fake or beauty is defined by any color, size and shape.
# Otherwise:
# **fat foodie**
# **Makeup Junkie**
# **Always happy**
# **Gemini**
# **procrastinator**
# **Singer (at times)**
# **Dancer (at times)**
# **Play Ukulele (occasionally)**
# **hate to show off**
# **📸 Insta: Sharnya_malhotra**
# **Friends Fan**
# ***Isn't that just kick you in the crotch,, spit on your neck fantastic**"""
 
 
bio1 = list(bio) 
 
 
to_remove = ["*", "$", "#", "&", "^", "!", "-", "=", "(", ")", "/", "?", ",", "'", '"', "|", ";", "<", ">", "\n", "\t", "*"]
 



def remove_all_special_characters(bio):
    for char in to_remove:
        bio = bio.replace(char, "")
    return bio

print(remove_all_special_characters(bio))