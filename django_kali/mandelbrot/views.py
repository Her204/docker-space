import os
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import matplotlib.image as mpimg
from matplotlib import colors
from scipy import ndimage
from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objects as go
import pandas as pd
import plotly
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def plot_fao_2(response):
    def mandelbrot_set(text,xmin,xmax,ymin,ymax,xn,yn,maxiter,number,horizon=2.0):

        X = np.linspace(xmin,xmax,xn,dtype=np.float32)
        Y = np.linspace(ymin,ymax,yn,dtype=np.float32)
        C = X + Y[:,None]*1j
        N = np.zeros(C.shape,dtype=int)
        Z = np.zeros(C.shape,np.complex64)
        for n in range(maxiter):
            I = np.less(abs(Z),horizon)
            N[I] = n
            Z[I] = eval("{}Z[I]{}**number +C[I]".format(text[0],text[1]))
        N[n==maxiter-1] = 0

        return Z,N
    def img(text_change,a):
        xmin,xmax,xn=-2.75,+2.75,300
        ymin,ymax,yn=-1.75,+1.75,250
        maxiter = 400
        horizon = 1.4e+3.5
        log_horizon = np.log(np.log(horizon))/np.log(a)

        Z,N = mandelbrot_set(text_change,xmin,
                     xmax,ymin,ymax,xn,
                     yn,maxiter,a,horizon)
        with np.errstate(invalid="ignore"):
            M = np.nan_to_num(N+1-np.log(np.log(abs(Z)))/np.log(a)+log_horizon)

        light = colors.LightSource(azdeg=315,altdeg=10)
        M = light.shade(M,cmap=plt.cm.hot,vert_exag=1.5,
            norm=colors.PowerNorm(0.3),blend_mode="hsv")

        #data = px.imshow(M*255)
        #fig = go.Figure(data=data)
        data = go.Image(z=M*255)
        return data

    def sliders_img(text_change,a):
        frames = []
        for a_12 in range(10+1):
            data = img(text_change,a+a_12/10)
            print(a_12,text_change)
            #fig.add_trace(data)
            frames.append(data)
            #fig.update_layout(autosize=True)
        fig = go.Figure(data=[frames[0]],
                        layout=go.Layout(
                            updatemenus=[dict(
                                type="buttons",
                                buttons=[dict(
                                    label="Play",
                                    method="animate",
                                    args=[None])])]),
                        frames=[go.Frame(data=[frame]) for frame in frames[1:]]
                        )
        fig.update_layout(height=700,autosize=True,
                         #sliders=sliders,
                         title="Mandelbrot set plot {}".format(a).upper())

        plot_div = plot(fig,output_type="div",
                        include_plotlyjs=False)
        return plot_div

    context = {}
    if response.POST.get("list_values"):
        txt_2 = response.POST.get("newvalue")
        b = float(txt_2)
        cases = [
             ["",""],
             #["np.tan(",")"],
             #["np.cosh(",")"]
             ]
        context = {"plot{}".format(i+1):sliders_img(a,b) for i,a in enumerate(cases)}
    #context = {"plot{}".format(x-1):cardioid(x) for x in range(2,6)}
    return render(response,"mandelbrot/welcome.html",context)
