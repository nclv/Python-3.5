# -*- coding: utf-8  -*-


"""
    Function for generating a quadrature rule on the triangle

    Copyright (C) 2013 Greg von Winckel

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Created: Sun May 26 11:26:58 MDT 2013

"""


import numpy as np
import orthopoly as op

def triquad(n):
    """
        Compute the quadrature nodes and weights for integrating a
        function f(x,y) over a triangle with vertices {(-1,-1),(-1,1),(1,-1)}

        The quadrature rule is generated by using a Duffy transformation to map
        the square to the triangle 
    """
    alphax,betax = op.rec_jacobi(n,0,1)
    x,wx = op.gauss(alphax,betax)
    x = (1+x)/2
    wx = wx/2

    alphat,betat = op.rec_jacobi(n,0,0)
    t,wt = op.gauss(alphat,betat)
    t = (1+t)/2
    wt = wt

    tt, xx = np.meshgrid(t,x)
    yy = xx*tt

    xx = 1-2*xx
    yy = 2*yy-1

    ww = np.outer(wx,wt)
    
    xx = xx.flatten()
    yy = yy.flatten()
    ww = ww.flatten()

    return xx,yy,ww

