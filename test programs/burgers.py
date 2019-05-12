#! /usr/bin/env python
#
def resid_burgers ( nu, n, x, y, z, t ):

#*****************************************************************************80
#
## RESID_BURGERS: Burgers Navier Stokes residual.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Martin Bazant, Henry Moffatt,
#    Exact solutions of the Navier-Stokes equations having steady vortex structures,
#    Journal of Fluid Mechanics,
#    Volume 541, pages 55-64, 2005.
#
#    Johannes Burgers,
#    A mathematical model illustrating the theory of turbulence,
#    Advances in Applied Mechanics,
#    Volume 1, pages 171-199, 1948.
#
#  Parameters:
#
#    Input, real NU, the viscosity.
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
  from r8_erf import r8_erf
#
#  Form the functions and derivatives.
#
  u =   2.0 * x
  ux =  2.0 * np.ones ( n )
  uxx = np.zeros ( n )
  uy =  np.zeros ( n )
  uyy = np.zeros ( n )
  uz =  np.zeros ( n )
  uzz = np.zeros ( n )
  ut =  np.zeros ( n )

  v =   - 2.0 * y
  vx =  np.zeros ( n )
  vxx = np.zeros ( n )
  vy =  - 2.0 * np.ones ( n )
  vyy = np.zeros ( n )
  vz =  np.zeros ( n )
  vzz = np.zeros ( n )
  vt =  np.zeros ( n )

  w = np.zeros ( n )
  for i in range ( 0, n ):
    w[i] =   r8_erf ( y[i] / np.sqrt ( nu ) )
  wx =  np.zeros ( n )
  wxx = np.zeros ( n )
  wy =    2.0 * np.sqrt ( 1.0 / nu / np.pi )     * np.exp ( - y ** 2 / nu )
  wyy = - 4.0 * np.sqrt ( 1.0 / nu / np.pi ) * y * np.exp ( - y ** 2 / nu ) / nu
  wz =  np.zeros ( n )
  wzz = np.zeros ( n )
  wt =  np.zeros ( n )

  p = - 2.0 * ( x ** 2 + y ** 2 )
  px = - 4.0 * x
  py = - 4.0 * y
  pz = np.zeros ( n )
#
#  Evaluate the residuals.
#
  ur = ut + u * ux + v * uy + w * uz + px - nu * ( uxx + uyy + uzz )
  vr = vt + u * vx + v * vy + w * vz + py - nu * ( vxx + vyy + vzz )
  wr = wt + u * wx + v * wy + w * wz + pz - nu * ( wxx + wyy + wzz )
  pr = ux + vy + wz

  return ur, vr, wr, pr

def resid_burgers_test ( ):

#*****************************************************************************80
#
## RESID_BURGERS_TEST samples the Burgers residual at the initial time.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_uniform_ab import r8vec_uniform_ab

  nu = 0.25

  print ( '' )
  print ( 'RESID_BURGERS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  RESID_BURGERS evaluates the Burgers residual.' )
  print ( '  Sample at the initial time T = 0, using a region that is' )
  print ( '  the cube centered at (0,0,0) with "radius" 1.0,' )
  print ( '  Viscosity NU = %g' % ( nu ) )

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  z, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  t = np.zeros ( n )

  ur, vr, wr, pr = resid_burgers ( nu, n, x, y, z, t )

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
  print ( 'RESID_BURGERS_TEST:' )
  print ( '  Normal end of execution.' )
  return

def uvwp_burgers ( nu, n, x, y, z, t ):

#*****************************************************************************80
#
## UVWP_BURGERS evaluates the Burgers solution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 July 2015
#
#  Author:
#
#    John Burkardt
#
#  Reference:
#
#    Martin Bazant, Henry Moffatt,
#    Exact solutions of the Navier-Stokes equations having steady vortex structures,
#    Journal of Fluid Mechanics,
#    Volume 541, pages 55-64, 2005.
#
#    Johannes Burgers,
#    A mathematical model illustrating the theory of turbulence,
#    Advances in Applied Mechanics,
#    Volume 1, pages 171-199, 1948.
#
#  Parameters:
#
#    Input, real NU, the kinematic viscosity.
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
  from r8_erf import r8_erf

  u =   2.0 * x
  v =   - 2.0 * y
  w = np.zeros ( n )
  for i in range ( 0, n ):
    w[i] =   r8_erf ( y[i] / np.sqrt ( nu ) )
  p = - 2.0 * ( x ** 2 + y ** 2 )

  return u, v, w, p

def uvwp_burgers_test ( ):

#*****************************************************************************80
#
## UVWP_BURGERS_TEST samples the Burgers solution.
#
#  Licensing:
#
#    This code is distributed under the GNU LGPL license.
#
#  Modified:
#
#    30 July 2015
#
#  Author:
#
#    John Burkardt
#
  import numpy as np
  import platform
  from r8vec_uniform_ab import r8vec_uniform_ab

  nu = 0.25

  print ( '' )
  print ( 'UVWP_BURGERS_TEST' )
  print ( '  Python version: %s' % ( platform.python_version ( ) ) )
  print ( '  UVWP samples the Burgers solution.' )
  print ( '  Estimate the range of velocity and pressure' )
  print ( '  at the initial time T = 0, using a region that is' )
  print ( '  the cube centered at (0,0,0) with "radius" 1.0,' )
  print ( '  Viscosity NU = %g' % ( nu ) )

  n = 1000
  x_lo = -1.0
  x_hi = +1.0
  seed = 123456789
  x, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  y, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  z, seed = r8vec_uniform_ab ( n, x_lo, x_hi, seed )
  t = np.zeros ( n )

  u, v, w, p = uvwp_burgers ( nu, n, x, y, z, t )

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
  print ( 'UVWP_BURGERS_TEST:' )
  print ( '  Normal end of execution.' )
  return

if ( __name__ == '__main__' ):
  from timestamp import timestamp
  timestamp ( )
  uvwp_burgers_test ( )
  resid_burgers_test ( )
  timestamp ( )

