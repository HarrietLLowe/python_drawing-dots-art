import colorgram

colors = colorgram.extract('Addictive---detail-of-Dam-007.jpg', 30)

# this is the long way of doing this
# first_color = colors[0]
# rgb_identify = first_color.rgb
# first_color_colors = ()
# red = rgb_identify[0]
# green = rgb_identify[1]
# blue = rgb_identify[2]
#
# first_color_colors = (red, green, blue)
# rbg = [first_color_colors]

# the tidy way in a for loop

rbg = []

for n in range(0, 30):
    n_color = colors[n]
    rgb_identify = n_color.rgb
    n_color_colors = ()
    red = rgb_identify[0]
    green = rgb_identify[1]
    blue = rgb_identify[2]
    n_color_colors = (red, green, blue)
    rbg.append(n_color_colors)

print(rbg)
