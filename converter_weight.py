
# coding: utf-8

# In[ ]:


EARTHG = 9.81
MOONG = 1.62
MARSG = 3.77
JUPITERG = 25.95
SUNG = 274.13
weight = float(input('Enter weight on Earth: '))
moon_w = weight*MOONG/EARTHG
mars_w = weight*MARSG/EARTHG
jupiter_w = weight*JUPITERG/EARTHG
sun_w = weight*SUNG/EARTHG
weight_L = [moon_w, mars_w, jupiter_w, sun_w]
we = int(input('Enter 1 for moon, 2 for Mars, 3 for Jupiter, or 4 for the Sun:'))
print('Your converted weight is ',weight_L[we - 1],'pounds.' )


# In[ ]:


EARTHG = 9.81
MOONG = 1.62
MARSG = 3.77
JUPITERG = 25.95
SUNG = 274.13
weight = float(input('Enter weight on Earth: '))
moon_w = round(weight*MOONG/EARTHG,2) 
mars_w = round(weight*MARSG/EARTHG, 2)
jupiter_w = round(weight*JUPITERG/EARTHG, 2)
sun_w = round(weight*SUNG/EARTHG, 2)
weight_L = [moon_w, mars_w, jupiter_w, sun_w]
we = int(input('Enter 1 for moon, 2 for Mars, 3 for Jupiter, or 4 for the Sun:'))
print('Your converted weight is ',weight_L[we - 1],'pounds.' )

