import pygame
import math

default_fontname = "arial"
default_fontsize = 12
title_fontsize = 14

def draw_text(str, coords, screen, fontname=default_fontname, fontsize = default_fontsize):
    (x,y) = coords
    font = pygame.font.SysFont(fontname, fontsize)
    screen.blit(font.render(str, True, "black"), (x, y))


def number_format(prob):
    if prob >0:
        expnt = math.floor(math.log(prob, 10))
    else:
        return '0'
    numeral = round(prob / math.pow(10, expnt),1)
    s = str(numeral)+'e'+str(expnt)
    return s

def histogram(screen,boundary,bins,vals,title = '', max_y=None, probability_density_function = None):
    (start_x, start_y, width, height) = boundary
    pygame.draw.rect(screen,"black",[start_x,start_y,width,height],2)
    bin_width = [float(x)-float(bins[i-1]) for i,x in enumerate(bins) if i>0]
    bin_width_avg = sum(bin_width)/len(bin_width)
    bin_width.append(bin_width[-1]) #asssuming that the width of the last bin is the same as the one before it, because only have left edge of all bins

    bar_start_x = start_x + int(0.1*width)
    bar_start_y = start_y + int(0.1*height)
    bar_gap = int(0.8*width/len(vals))
    bar_width = int(0.8*bar_gap)
    bar_height = int(0.8*height)

    draw_text(title, (bar_start_x, start_y + int(0.05 * height)), screen, fontsize=title_fontsize)

    text_height = int(0.81*height)
    text_inc = round(len(bins)/10)

    max_v = max(vals)
    sum_v = sum(vals)
    if max_y is None:
        max_y = max_v/sum_v/bin_width_avg#.01

    for i in range(10+1):
        prob = i/10*max_y
        if prob<=max_y:
            y_coord = bar_start_y + bar_height - int(bar_height * prob/max_y)
            draw_text(number_format(prob),(start_x+ int(0.02 * width),y_coord), screen)
            pygame.draw.line(screen, "black", (start_x+ int(0.075 * width),y_coord),(start_x+ int(0.9 * width),y_coord))

    for i,v in enumerate(vals):
        bar_x = int(bar_start_x+i*bar_gap)
        bar_y = int(bar_height * v / sum_v/bin_width[i]/max_y)
        #Note y-axis inverted as per pygame
        pygame.draw.rect(screen, "blue", [bar_x, bar_start_y + bar_height - bar_y, bar_width, bar_y ])

        if int(i/text_inc) == i/text_inc:
            draw_text(number_format(bins[i]), (bar_x, bar_start_y + text_height), screen)
            pygame.draw.line(screen, "black", (bar_x,bar_start_y),(bar_x,bar_start_y + text_height))
    pygame.draw.line(screen, "black", (bar_start_x + int(0.8*width), bar_start_y), (bar_start_x + int(0.8*width), bar_start_y + text_height))
    #print(vals)

    if probability_density_function is not None:
        num_pdf_points = 100
        x_val_delta = (bins[1]-bins[0])
        prev_point = (bar_start_x, bar_start_y+ bar_height)
        for i in range(num_pdf_points+1):
            x_pixel=bar_start_x + int(0.8*width*i/num_pdf_points)
            x_val=bins[0]+ (bins[1]-bins[0])*i/num_pdf_points*len(bins)
            y_val = probability_density_function(x_val)#* x_val_delta
            y_pixel = bar_start_y + bar_height - int(bar_height * y_val/max_y)
            next_point = (x_pixel, y_pixel)
            pygame.draw.line(screen, "red", prev_point, next_point)
            prev_point =next_point