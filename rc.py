import os

VON_BASE_PATH = "/home/evan/Documents/Oly-Math/Database/" # TODO for public, use better
EDITOR = os.environ.get('EDITOR','vim') #that easy!

SEPERATOR = '\n---\n'
NSEPERATOR = '\n' + SEPERATOR + '\n'

TAG_HINT_TEXT = """# Some hints for tags:
#
# ** Sources: @mine @obscure @rare @secret
# ** Problem Shape: @yesno @find @construct @bestpossible @hardanswer
# Quality: @favorite > @nice > @good > @ugly @work
# Philosophy: @instructive @reliable @justdoit @magic
# Philosophy': @smallcases @equalitycase @scouting @meta @dumb
# Philosophy'': @wishful @criticalclaim  @stronger @thinkbig
# Solution Method: @induct @manysolutions @magic @inefficient  @explicit @compute
# More tags: @pitfall @troll @intuitive @size @weak @maturity
# NT tags: @primes @p#adic @QR @pell @smallestprime @mods @fermat @zsig @cyclotomic @divis @order @christmas @CRT
# Algebra tags: @polynomial @trig @roots @calculus @continuity @irreducible @exactsum @manip
# Ineq tags: @holder @CDN @schur @AMGM @Titu @homogenize @dehomogenize @SOS @jensen @isofudge
# Combinatorics: @greedy @optimization @additivecombo @extreme @invariant @pigeonhole @parity @graph @adhoc @EV @combogeo @hall @grid @rigid
# Geometry tags
  # Part I and II: @anglechase @simtri @pop @homothety @cevalaus @trig @complex @bary @length
  # Part III: @inversion @polar @projective @harmonic @miquel @spiralsim @mixtilinear"""

USE_COLOR = True