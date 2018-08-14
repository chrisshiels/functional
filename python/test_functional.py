# 'test_functional.py'.
# Chris Shiels.


import pytest


import functional


def test_all_recursive():
  assert functional.all_recursive(lambda e: e % 2 == 0,
                                  []) == \
         False
  assert functional.all_recursive(lambda e: e % 2 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.all_recursive(lambda e: e % 3 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         False
  with pytest.raises(RuntimeError):
    functional.all_recursive(lambda e: e, [ True ] * 1000)


def test_all_accumulator():
  assert functional.all_accumulator(lambda e: e % 2 == 0,
                                    []) == \
         False
  assert functional.all_accumulator(lambda e: e % 2 == 0,
                                    [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.all_accumulator(lambda e: e % 3 == 0,
                                    [ 2, 4, 6, 8, 10 ]) == \
         False
  assert functional.all_accumulator(lambda e: e,
                                    [ True ] * 1000) == \
         True


def test_all_callbacks():
  assert functional.all_callbacks(lambda e: e % 2 == 0,
                                  []) == \
         False
  assert functional.all_callbacks(lambda e: e % 2 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.all_callbacks(lambda e: e % 3 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         False
  assert functional.all_callbacks(lambda e: e,
                                  [ True ] * 1000) == \
         True


def test_any_recursive():
  assert functional.any_recursive(lambda e: e % 2 == 0,
                                  []) == \
         False
  assert functional.any_recursive(lambda e: e % 2 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.any_recursive(lambda e: e % 3 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         True
  with pytest.raises(RuntimeError):
    functional.any_recursive(lambda e: e, [ False ] * 1000)


def test_any_accumulator():
  assert functional.any_accumulator(lambda e: e % 2 == 0,
                                    []) == \
         False
  assert functional.any_accumulator(lambda e: e % 2 == 0,
                                    [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.any_accumulator(lambda e: e % 3 == 0,
                                    [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.any_accumulator(lambda e: e,
                                    [ True ] * 1000) == \
         True


def test_any_callbacks():
  assert functional.any_callbacks(lambda e: e % 2 == 0,
                                  []) == \
         False
  assert functional.any_callbacks(lambda e: e % 2 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.any_callbacks(lambda e: e % 3 == 0,
                                  [ 2, 4, 6, 8, 10 ]) == \
         True
  assert functional.any_callbacks(lambda e: e,
                                  [ True ] * 1000) == \
         True


def test_flatten_recursive():
  assert functional.flatten_recursive([]) == \
         []
  assert functional.flatten_recursive([ 1, 2, 3 ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_recursive([ [ 1, 2 ], 3 ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_recursive([ 1, [ 2, 3 ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_recursive([ 1, [ 2, [ 3 ] ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_recursive([ [ [ 1 ], [ 2 ], [ 3 ] ] ]) == \
         [ 1, 2, 3 ]
  with pytest.raises(RuntimeError):
    functional.flatten_recursive([ [ 1 ] ] * 1000)


def test_flatten_accumulator():
  assert functional.flatten_accumulator([]) == \
         []
  assert functional.flatten_accumulator([ 1, 2, 3 ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_accumulator([ [ 1, 2 ], 3 ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_accumulator([ 1, [ 2, 3 ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_accumulator([ 1, [ 2, [ 3 ] ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_accumulator([ [ [ 1 ], [ 2 ], [ 3 ] ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_accumulator([ [ 1 ] ] * 1000) == \
         [ 1 ] * 1000


def test_flatten_callbacks():
  assert functional.flatten_callbacks([]) == \
         []
  assert functional.flatten_callbacks([ 1, 2, 3 ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_callbacks([ [ 1, 2 ], 3 ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_callbacks([ 1, [ 2, 3 ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_callbacks([ 1, [ 2, [ 3 ] ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_callbacks([ [ [ 1 ], [ 2 ], [ 3 ] ] ]) == \
         [ 1, 2, 3 ]
  assert functional.flatten_callbacks([ [ 1 ] ] * 1000) == \
         [ 1 ] * 1000


def test_range_recursive():
  assert functional.range_recursive(0) == \
         []
  assert functional.range_recursive(10) == \
         [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  assert functional.range_recursive(0, 10) == \
         [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  assert functional.range_recursive(0, 10, 1) == \
         [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  assert functional.range_recursive(0, 10, 2) == \
         [ 0, 2, 4, 6, 8 ]
  assert functional.range_recursive(0, 10, 3) == \
         [ 0, 3, 6, 9 ]
  assert functional.range_recursive(10, 0, -1) == \
         [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
  assert functional.range_recursive(1, 11) == \
         [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
  with pytest.raises(RuntimeError):
    functional.range_recursive(1, 1001)


def test_range_accumulator():
  assert functional.range_accumulator(0) == \
         []
  assert functional.range_accumulator(10) == \
         [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  assert functional.range_accumulator(0, 10) == \
         [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  assert functional.range_accumulator(0, 10, 1) == \
         [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  assert functional.range_accumulator(0, 10, 2) == \
         [ 0, 2, 4, 6, 8 ]
  assert functional.range_accumulator(0, 10, 3) == \
         [ 0, 3, 6, 9 ]
  assert functional.range_accumulator(10, 0, -1) == \
         [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
  assert functional.range_accumulator(1, 11) == \
         [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
  assert len(functional.range_accumulator(1, 1001)) == 1000


def test_range_callbacks():
  assert functional.range_callbacks(0) == \
         []
  assert functional.range_callbacks(10) == \
         [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  assert functional.range_callbacks(0, 10) == \
         [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  assert functional.range_callbacks(0, 10, 1) == \
         [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
  assert functional.range_callbacks(0, 10, 2) == \
         [ 0, 2, 4, 6, 8 ]
  assert functional.range_callbacks(0, 10, 3) == \
         [ 0, 3, 6, 9 ]
  assert functional.range_callbacks(10, 0, -1) == \
         [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
  assert functional.range_callbacks(1, 11) == \
         [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
  assert len(functional.range_callbacks(1, 1001)) == 1000


def test_reduce_accumulator():
  assert functional.reduce_accumulator(lambda a, e: a + e,
                                       functional.range(1, 11), 0) == \
         55
  assert functional.reduce_accumulator(lambda a, e: a + e,
                                       functional.range(1, 11)) == \
         55
  assert functional.reduce_accumulator(lambda a, e: a + e,
                                       [ [ 1 ], [ 2, 3 ], [ 4, 5, 6 ] ]) == \
         [ 1, 2, 3, 4, 5, 6 ]
  assert functional.reduce_accumulator(lambda a, e: a + len(e),
                                       [ [ 1 ], [ 2, 3 ], [ 4, 5, 6 ] ], 0) == \
         6
  assert functional.reduce_accumulator(lambda a, e: a + e,
                                       functional.range(1, 1001),
                                       0) == \
         500500


def test_map():
  assert functional.map(lambda e: e * 2,
                        functional.range(1, 11)) == \
         [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 ]
  assert functional.map(lambda e: e,
                        [ [ 1 ], [ 2 ], [ 3 ] ]) == \
         [ [ 1 ], [ 2 ], [ 3 ] ]


def test_filter():
  assert functional.filter(lambda e: e % 2 == 0,
                           functional.range(1, 11)) == \
         [ 2, 4, 6, 8, 10 ]
  assert functional.filter(lambda e: e % 2 == 1,
                           functional.range(1, 11)) == \
         [ 1, 3, 5, 7, 9 ]
  assert functional.filter(lambda e: len(e) != 0,
                           [ [ 1 ], [], [ 2 ], [], [ 3 ] ]) == \
         [ [ 1 ], [ 2 ], [ 3 ] ]


def test_partition():
  assert functional.partition(lambda e: e % 3 == 0,
                              functional.range(1, 11)) == \
         [ [ 3, 6, 9 ], [ 1, 2, 4, 5, 7, 8, 10 ] ]
  assert functional.partition(lambda e: e % 3 != 0,
                              functional.range(1, 11)) == \
         [ [ 1, 2, 4, 5, 7, 8, 10 ], [ 3, 6, 9 ] ]
  assert functional.partition(lambda e: e == 0,
                              functional.range(1, 11)) == \
         [ [], [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] ]

  assert functional.partition(lambda e: len(e) > 1,
                              [ [ 1 ], [ 1, 2 ], [ 1, 2, 3 ] ]) == \
         [ [ [ 1, 2 ], [ 1, 2, 3 ] ], [ [ 1 ] ] ]


def test_split():
  assert functional.split(lambda e: e % 10 == 0,
                          []) == \
         []
  assert functional.split(lambda e: e % 1 == 0,
                          functional.range(1, 11)) == \
         []
  assert functional.split(lambda e: e % 2 == 0,
                          functional.range(1, 11)) == \
         [ [ 1 ], [ 3 ], [ 5 ], [ 7 ], [ 9 ] ]
  assert functional.split(lambda e: e % 3 == 0,
                          functional.range(1, 11)) == \
         [ [ 1, 2 ], [ 4, 5 ], [ 7, 8 ], [ 10 ] ]


def test_reverse():
  assert functional.reverse(functional.range(1, 11)) ==  \
         [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
  assert functional.reverse([ [ 1, 2 ], [ 3, 4 ], [ 5, 6 ] ]) == \
         [ [ 5, 6 ], [ 3, 4 ], [ 1, 2 ] ]


def test_sort_recursive():
  assert functional.sort_recursive(lambda m, n: m <= n,
                                   [1, 10, 2, 9, 3, 8, 4, 7, 5, 6 ]) == \
         functional.range(1, 11)
  assert functional.sort_recursive(lambda m, n: len(m) <= len(n),
                                   [ [ 1, 2, 3], [ 1, 2 ], [ 1 ] ]) == \
         [ [ 1 ], [ 1, 2 ],  [ 1, 2, 3 ] ]
  with pytest.raises(RuntimeError):
    functional.sort_recursive(lambda m, n: m <= n,
                              range(1000, 0, -1))


def test_sort_callbacks():
  assert functional.sort_callbacks(lambda m, n: m <= n,
                                   [1, 10, 2, 9, 3, 8, 4, 7, 5, 6 ]) == \
         functional.range(1, 11)
  assert functional.sort_callbacks(lambda m, n: len(m) <= len(n),
                                   [ [ 1, 2, 3], [ 1, 2 ], [ 1 ] ]) == \
         [ [ 1 ], [ 1, 2 ],  [ 1, 2, 3 ] ]
  assert functional.sort_callbacks(lambda m, n: m <= n,
                                   range(1000, 0, -1)) == \
         range(1, 1001)


def test_unique():
  assert functional.unique([ 5, 1, 4, 2, 3, 3, 2, 4, 1, 5 ]) == \
         [ 5, 1, 4, 2, 3 ]


def test_zip():
  a = [ [ 1, 2, 3, 4 ],
        [ 5, 6, 7, 8 ] ]
  a1 = [ [ 1, 5 ],
         [ 2, 6 ],
         [ 3, 7 ],
         [ 4, 8 ] ]
  assert functional.zip(*a) == \
         a1
  assert functional.zip(*functional.zip(*a)) == a


def test_permutations():
  assert functional.permutations([]) == \
         []
  assert functional.permutations([ 1 ]) == \
         [ [ 1 ] ]
  assert functional.permutations([ 1, 2 ]) == \
         [ [ 1, 2 ], [ 2, 1 ] ]
  assert functional.permutations([ 1, 2, 3 ]) == \
         [ [ 1, 2, 3 ],
           [ 1, 3, 2 ],
           [ 2, 1, 3 ],
           [ 2, 3, 1 ],
           [ 3, 1, 2 ],
           [ 3, 2, 1 ] ]
  assert functional.permutations([ 1, 2, 3, 4 ]) == \
         [ [ 1, 2, 3, 4 ],
           [ 1, 2, 4, 3 ],
           [ 1, 3, 2, 4 ],
           [ 1, 3, 4, 2 ],
           [ 1, 4, 2, 3 ],
           [ 1, 4, 3, 2 ],
           [ 2, 1, 3, 4 ],
           [ 2, 1, 4, 3 ],
           [ 2, 3, 1, 4 ],
           [ 2, 3, 4, 1 ],
           [ 2, 4, 1, 3 ],
           [ 2, 4, 3, 1 ],
           [ 3, 1, 2, 4 ],
           [ 3, 1, 4, 2 ],
           [ 3, 2, 1, 4 ],
           [ 3, 2, 4, 1 ],
           [ 3, 4, 1, 2 ],
           [ 3, 4, 2, 1 ],
           [ 4, 1, 2, 3 ],
           [ 4, 1, 3, 2 ],
           [ 4, 2, 1, 3 ],
           [ 4, 2, 3, 1 ],
           [ 4, 3, 1, 2 ],
           [ 4, 3, 2, 1 ] ]


def test_compose():
  def valueadd1(v):
    return v + 1

  def valuemultiply2(v):
    return v * 2

  assert functional.compose(valueadd1, valuemultiply2)(1) == 4


def test_pipe():
  def valueadd1(v):
    return v + 1

  def valuemultiply2(v):
    return v * 2

  def listadd1(l):
    return functional.map(lambda e: e + 1, l)

  def listmultiply2(l):
    return functional.map(lambda e: e * 2, l)

  assert functional.pipe([ valueadd1,
                           valuemultiply2,
                           valueadd1 ])(1) == 5
  assert functional.pipe([ listadd1,
                           listmultiply2,
                           listadd1 ])(functional.range(1, 11)) == \
         [ 5, 7, 9, 11, 13, 15, 17, 19, 21, 23 ]


# Note pipe2 is not compatible with the trampoline implementation of reduce.
#def test_pipe2():
#  def valueadd1(v):
#    return v + 1
#
#  def valuemultiply2(v):
#    return v * 2
#
#  def listadd1(l):
#    return functional.map(lambda e: e + 1, l)
#
#  def listmultiply2(l):
#    return functional.map(lambda e: e * 2, l)
#
#  assert functional.pipe2([ valueadd1,
#                           valuemultiply2,
#                           valueadd1 ])(1) == 5
#  assert functional.pipe2([ listadd1,
#                           listmultiply2,
#                           listadd1 ])(functional.range(1, 11)) == \
#         [ 5, 7, 9, 11, 13, 15, 17, 19, 21, 23 ]


def test_pipemaybe():
  def valueadd1(v):
    return v + 1

  def valuenone(v):
    return None

  assert functional.pipemaybe([ valueadd1,
                                valueadd1,
                                valueadd1 ])(0) == 3
  assert functional.pipemaybe([ valueadd1,
                                valuenone,
                                valueadd1 ])(0) == None


def test_partial():
  def add(a, b):
    return a + b

  def add10(x):
    return add(x, 10)

  assert functional.map(add10,
                        functional.range(1, 11)) == \
         [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
  assert functional.map(functional.partial(add, 10),
                        functional.range(1, 11)) == \
         [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]


def test_curry():
  def args(*a):
    return a

  cargs = functional.curry(args, 5)
  cargsab = cargs('a')('b')
  assert cargsab('c')('d')('e') == ('a', 'b', 'c', 'd', 'e')
  assert cargsab('x')('y')('z') == ('a', 'b', 'x', 'y', 'z')
  assert cargsab('c')('d')('e') == ('a', 'b', 'c', 'd', 'e')
  assert cargsab('x')('y')('z') == ('a', 'b', 'x', 'y', 'z')


  def add(a, b):
    return a + b

  cadd = functional.curry(add)
  assert cadd(10)(5) == 15 and cadd(20)(5) == 25

  assert functional.map(functional.curry(add)(10),
                        functional.range(1, 11)) == \
         [ 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]


def test_factorial_recursive():
  assert functional.map(functional.factorial_recursive,
                        functional.range(1, 11)) == \
         [ 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800 ]
  with pytest.raises(RuntimeError):
    functional.factorial_recursive(1000)


def test_factorial_accumulator():
  assert functional.map(functional.factorial_accumulator,
                        functional.range(1, 11)) == \
         [ 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800 ]
  assert functional.factorial_accumulator(1000) == \
         402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461062892187960223838971476088506276862967146674697562911234082439208160153780889893964518263243671616762179168909779911903754031274622289988005195444414282012187361745992642956581746628302955570299024324153181617210465832036786906117260158783520751516284225540265170483304226143974286933061690897968482590125458327168226458066526769958652682272807075781391858178889652208164348344825993266043367660176999612831860788386150279465955131156552036093988180612138558600301435694527224206344631797460594682573103790084024432438465657245014402821885252470935190620929023136493273497565513958720559654228749774011413346962715422845862377387538230483865688976461927383814900140767310446640259899490222221765904339901886018566526485061799702356193897017860040811889729918311021171229845901641921068884387121855646124960798722908519296819372388642614839657382291123125024186649353143970137428531926649875337218940694281434118520158014123344828015051399694290153483077644569099073152433278288269864602789864321139083506217095002597389863554277196742822248757586765752344220207573630569498825087968928162753848863396909959826280956121450994871701244516461260379029309120889086942028510640182154399457156805941872748998094254742173582401063677404595741785160829230135358081840096996372524230560855903700624271243416909004153690105933983835777939410970027753472000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000L


def test_factorial_callbacks():
  assert functional.map(functional.factorial_callbacks,
                        functional.range(1, 11)) == \
         [ 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800 ]
  assert functional.factorial_callbacks(1000) == \
         402387260077093773543702433923003985719374864210714632543799910429938512398629020592044208486969404800479988610197196058631666872994808558901323829669944590997424504087073759918823627727188732519779505950995276120874975462497043601418278094646496291056393887437886487337119181045825783647849977012476632889835955735432513185323958463075557409114262417474349347553428646576611667797396668820291207379143853719588249808126867838374559731746136085379534524221586593201928090878297308431392844403281231558611036976801357304216168747609675871348312025478589320767169132448426236131412508780208000261683151027341827977704784635868170164365024153691398281264810213092761244896359928705114964975419909342221566832572080821333186116811553615836546984046708975602900950537616475847728421889679646244945160765353408198901385442487984959953319101723355556602139450399736280750137837615307127761926849034352625200015888535147331611702103968175921510907788019393178114194545257223865541461062892187960223838971476088506276862967146674697562911234082439208160153780889893964518263243671616762179168909779911903754031274622289988005195444414282012187361745992642956581746628302955570299024324153181617210465832036786906117260158783520751516284225540265170483304226143974286933061690897968482590125458327168226458066526769958652682272807075781391858178889652208164348344825993266043367660176999612831860788386150279465955131156552036093988180612138558600301435694527224206344631797460594682573103790084024432438465657245014402821885252470935190620929023136493273497565513958720559654228749774011413346962715422845862377387538230483865688976461927383814900140767310446640259899490222221765904339901886018566526485061799702356193897017860040811889729918311021171229845901641921068884387121855646124960798722908519296819372388642614839657382291123125024186649353143970137428531926649875337218940694281434118520158014123344828015051399694290153483077644569099073152433278288269864602789864321139083506217095002597389863554277196742822248757586765752344220207573630569498825087968928162753848863396909959826280956121450994871701244516461260379029309120889086942028510640182154399457156805941872748998094254742173582401063677404595741785160829230135358081840096996372524230560855903700624271243416909004153690105933983835777939410970027753472000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000L


def test_fibonacci():
  assert functional.map(functional.fibonacci, functional.range(1, 11)) == \
         [ 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 ]


def test_memoizedfibonacci():
  assert functional.memoizedfibonacci(50) == \
         20365011074


def test_primes():
  assert functional.primes(20) == \
         [ 2, 3, 5, 7, 11, 13, 17, 19 ]


def test_ispalindrome():
  assert functional.ispalindrome('tattarrattat') == \
         True
