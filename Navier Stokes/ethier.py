#! /usr/bin/env python
#
def resid_ethier ( a, d, n, x, y, z, t ):

#*****************************************************************************80
#
## RESID_ETHIER evaluates the Ethier residual.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    C Ross Ethier, David Steinman,
#    Exact fully 3D Navier-Stokes solutions for benchmarking,
#    International Journal for Numerical Methods in Fluids,
#    Volume 19, Number 5, March 1994, pages 369-375.
#
#  Parameters:
#
#    Input, real A, D, the parameters.  Sample values are A = PI/4 and
#    D = PI/2.
#
#    Input, integer N, the number of points at which the solution is to
#    be evaluated.
#
#    Input, real X(N), Y(N), Z(N), the coordinates of the points.
#
#    Input, real T(N), the time coordinates.
#
#    Output, real UR(N), VR(N), WR(N), PR(N), the residuals.
#
  import numpy as np
#
#  Make some temporaries.
#
  ex = np.exp ( a * x )
  ey = np.exp ( a * y )
  ez = np.exp ( a * z )

  e2x = np.exp ( 2.0 * a * x )
  e2y = np.exp ( 2.0 * a * y )
  e2z = np.exp ( 2.0 * a * z )

  e2t = np.exp  ( -       d * d * t )
  e4t = np.exp  ( - 2.0 * d * d * t )

  exy = np.exp ( a * ( x + y ) )
  eyz = np.exp ( a * ( y + z ) )
  ezx = np.exp ( a * ( z + x ) )

  sxy = np.sin ( a * x + d * y )
  syz = np.sin ( a * y + d * z )
  szx = np.sin ( a * z + d * x )

  cxy = np.cos ( a * x + d * y )
  cyz = np.cos ( a * y + d * z )
  czx = np.cos ( a * z + d * x )
#
#  Form the functions and derivatives.
#
  u =   -         a * (           ex * syz +         ez * cxy ) * e2t
  ux =  -         a * (       a * ex * syz -     a * ez * sxy ) * e2t
  uxx = -         a * (   a * a * ex * syz - a * a * ez * cxy ) * e2t
  uy =  -         a * (       a * ex * cyz -     d * ez * sxy ) * e2t
  uyy = -         a * ( - a * a * ex * syz - d * d * ez * cxy ) * e2t
  uz =  -         a * (       d * ex * cyz +     a * ez * cxy ) * e2t
  uzz =  -        a * ( - d * d * ex * syz + a * a * ez * cxy ) * e2t
  ut =  + d * d * a * (           ex * syz +         ez * cxy ) * e2t

  v =   -         a * (           ey * szx +         ex * cyz ) * e2t
  vx =  -         a * (       d * ey * czx +     a * ex * cyz ) * e2t
  vxx = -         a * ( - d * d * ey * szx + a * a * ex * cyz ) * e2t
  vy =  -         a * (       a * ey * szx -     a * ex * syz ) * e2t
  vyy = -         a * (   a * a * ey * szx - a * a * ex * cyz ) * e2t
  vz =  -         a * (       a * ey * czx -     d * ex * syz ) * e2t
  vzz =  -        a * ( - a * a * ey * szx - d * d * ex * cyz ) * e2t
  vt =  + d * d * a * (           ey * szx +         ex * cyz ) * e2t

  w =   -         a * (           ez * sxy +         ey * czx ) * e2t
  wx =  -         a * (       a * ez * cxy -     d * ey * szx ) * e2t
  wxx = -         a * ( - a * a * ez * sxy - d * d * ey * czx ) * e2t
  wy =  -         a * (       d * ez * cxy +     a * ey * czx ) * e2t
  wyy = -         a * ( - d * d * ez * sxy + a * a * ey * czx ) * e2t
  wz =  -         a * (       a * ez * sxy -     a * ey * szx ) * e2t
  wzz = -         a * (   a * a * ez * sxy - a * a * ey * czx ) * e2t
  wt =  + d * d * a * (           ez * sxy +         ey * czx ) * e2t

  p = - 0.5 * a * a * e4t * ( \
    + e2x + 2.0 * sxy * czx * eyz \
    + e2y + 2.0 * syz * cxy * ezx \
    + e2z + 2.0 * szx * cyz * exy )

  px = - 0.5 * a * a * e4t * ( \
    + 2.0 * a * e2x + 2.0 * a * cxy * czx * eyz - 2.0 * d * sxy * szx * eyz \
                    - 2.0 * a * syz * sxy * ezx + 2.0 * a * syz * cxy * ezx \
                    + 2.0 * d * czx * cyz * exy + 2.0 * a * szx * cyz * exy )

  py = - 0.5 * a * a * e4t * ( \
                    + 2.0 * d * cxy * czx * eyz + 2.0 * a * sxy * czx * eyz \
    + 2.0 * a * e2y + 2.0 * a * cyz * cxy * ezx - 2.0 * d * syz * sxy * ezx \
                    - 2.0 * a * szx * syz * exy + 2.0 * a * szx * cyz * exy )

  pz = - 0.5 * a * a * e4t * ( \
                    - 2.0 * a * sxy * szx * eyz + 2.0 * a * sxy * czx * eyz \
                    + 2.0 * d * cyz * cxy * ezx + 2.0 * a * syz * cxy * ezx \
    + 2.0 * a * e2z + 2.0 * a * czx * cyz * exy - 2.0 * d * szx * syz * exy )
#
#  Evaluate the residuals.
#
  ur = ut + u * ux + v * uy + w * uz + px - ( uxx + uyy + uzz )
  vr = vt + u * vx + v * vy + w * vz + py - ( vxx + vyy + vzz )
  wr = wt + u * wx + v * wy + w * wz + pz - ( wxx + wyy + wzz )
  pr = ux + vy + wz;

  return ur, vr, wr, pr

def resid_ethier_test ( ):

#*****************************************************************************80
#
## RESID_ETHIER_TEST samples the Ethier residual.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_uniform_ab import r8vec_uniform_ab

  a = np.pi / 4.0
  d = np.pi / 2.0

  print ( '' )
  print ( 'RESID_ETHIER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RESID_ETHIER evaluates the Ethier residual.' )
  print ( '  Sample the residuals' )
  print ( '  at the initial time T = 0, using a region that is' )
  print ( '  the cube centered at (0,0,0) with "radius" 1.0,' )
  print ( '  Parameter A = %g' % ( a ) )
  print ( '  Parameter D = %g' % ( d ) )

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  z, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  t = np.zeros ( n )

  ur, vr, wr, pr = resid_ethier ( a, d, n, x, y, z, t )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  Ur:  %14.6g  %14.6g' % ( np.min ( np.abs ( ur ) ), np.max ( np.abs ( ur ) ) ) )
  print ( '  Vr:  %14.6g  %14.6g' % ( np.min ( np.abs ( vr ) ), np.max ( np.abs ( vr ) ) ) )
  print ( '  Wr:  %14.6g  %14.6g' % ( np.min ( np.abs ( wr ) ), np.max ( np.abs ( wr ) ) ) )
  print ( '  Pr:  %14.6g  %14.6g' % ( np.min ( np.abs ( pr ) ), np.max ( np.abs ( pr ) ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'RESID_ETHIER_TEST:' )
  print ( '  Normal end of execution.' )
  return

def uvwp_ethier ( a, d, n, x, y, z, t ):

#*****************************************************************************80
#
## UVWP_ETHIER evaluates the Ethier exact Navier Stokes solution.
#
#  Discussion:
#
#    The reference asserts that the given velocity and pressure fields
#    are exact solutions for the 3D incompressible time-dependent
#    Navier Stokes equations over any region.
#
#    To define a typical problem, one chooses a bounded spatial region 
#    and a starting time, and then imposes boundary and initial conditions
#    by referencing the exact solution appropriately.
#
#    In the reference paper, a calculation is made for the cube centered
#    at (0,0,0) with a "radius" of 1 unit, and over the time interval
#    from t = 0 to t = 0.1, with parameters a = PI/4 and d = PI/2,
#    and with Dirichlet boundary conditions on all faces of the cube.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    C Ross Ethier, David Steinman,
#    Exact fully 3D Navier-Stokes solutions for benchmarking,
#    International Journal for Numerical Methods in Fluids,
#    Volume 19, Number 5, March 1994, pages 369-375.
#
#  Parameters:
#
#    Input, real A, D, the parameters.  Sample values are A = PI/4 and
#    D = PI/2.
#
#    Input, integer N, the number of points at which the solution is to
#    be evaluated.
#
#    Input, real X(N), Y(N), Z(N), the coordinates of the points.
#
#    Input, real T(N), the time coordinates.
#
#    Output, real U(N), V(N), W(N), P(N), the velocity components and
#    pressure at each of the points.
#
  import numpy as np

  ex = np.exp ( a * x )
  ey = np.exp ( a * y )
  ez = np.exp ( a * z )

  e2t = np.exp  ( - d * d * t )

  exy = np.exp ( a * ( x + y ) )
  eyz = np.exp ( a * ( y + z ) )
  ezx = np.exp ( a * ( z + x ) )

  sxy = np.sin ( a * x + d * y )
  syz = np.sin ( a * y + d * z )
  szx = np.sin ( a * z + d * x )

  cxy = np.cos ( a * x + d * y )
  cyz = np.cos ( a * y + d * z )
  czx = np.cos ( a * z + d * x )

  u = - a * ( ex * syz + ez * cxy ) * e2t
  v = - a * ( ey * szx + ex * cyz ) * e2t
  w = - a * ( ez * sxy + ey * czx ) * e2t
  p = 0.5 * a * a * e2t * e2t * ( \
    + ex * ex + 2.0 * sxy * czx * eyz \
    + ey * ey + 2.0 * syz * cxy * ezx \
    + ez * ez + 2.0 * szx * cyz * exy )

  return u, v, w, p

def uvwp_ethier_test ( ):

#*****************************************************************************80
#
## UVWP_ETHIER_TEST samples the solution at the initial time.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    29 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_uniform_ab import r8vec_uniform_ab

  a = np.pi / 4.0
  d = np.pi / 2.0

  print ( '' )
  print ( 'UVWP_ETHIER_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UVWP_ETHIER evaluates the Ethier solution.' )
  print ( '  Estimate the range of velocity and pressure' )
  print ( '  at the initial time T = 0, using a region that is' )
  print ( '  the cube centered at (0,0,0) with "radius" 1.0,' )
  print ( '  Parameter A = %g' % ( a ) )
  print ( '  Parameter D = %g' % ( d ) )

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  z, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  t = np.zeros ( n )

  u, v, w, p = uvwp_ethier ( a, d, n, x, y, z, t )

  print ( '' )
  print ( '           Minimum       Maximum' )
  print ( '' )
  print ( '  U:  %14.6g  %14.6g' % ( np.min ( u ), np.max ( u ) ) )
  print ( '  V:  %14.6g  %14.6g' % ( np.min ( v ), np.max ( v ) ) )
  print ( '  W:  %14.6g  %14.6g' % ( np.min ( w ), np.max ( w ) ) )
  print ( '  P:  %14.6g  %14.6g' % ( np.min ( p ), np.max ( p ) ) )
#
#  Terminate.
#
  print ( '' )
  print ( 'UVWP_ETHIER_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  uvwp_ethier_test ( )
  resid_ethier_test ( )
  timestamp ( )

