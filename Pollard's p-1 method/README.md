## [Pollard's p -1 method](https://en.wikipedia.org/wiki/Pollard%27s_p_%E2%88%92_1_algorithm)
This is an algorithm mainly used to factorize integers.

Note at the time that this algorithm performed badly in factorizing a random large integer, 

but it is very efficient in decomposing a certain class of integers containing special properties.

That is when the integer n is in the form of n = p * q ,and each p and q are primes.

And at least one of prime factor p or q is the **B - smooth** integer.

Which means any prime factors in an integer n is smaller than the upper bound B.

For example:

p' = 166! + 1 is a large prime:

3393108684451898201198256093588573203239663555699420770196366208812326

5314176330336254535971207181169698868584991941607780111073928236261199

604691797570505851011072000000000000000000000000001

p' - 1 = 16!,the largest prime factor of p - 1 is 113.

Let us randomly choose an large prime integer q':

7578394827639262854447045607636194648484378082111835580924782350500439

0808774341362653359685918757006934527208925423198132690457051871181856

4647293902848534287414745856638704524838370773472487581534668358073347

6425686933211755869258874040154804896864211268215332501636615058119702

482753310449124694379

and then let n' = p' * q' ,n = 

2571431730386812900136324938450478232038365678813856028477160771585434

8808168314898157356511471474954106461989172209619382609685709667836599

1370601763161599424417037132775925823221651324653921614124764250898539

9210281984122469511913868151180247720193772385121048462764822597577321

5052631467801714354087686754618607400417207300999031972386341801401606

4586879734156855713693366495832106604263909399149711791485291526578334

2566300963911895773530586979034315217817793461197024827533104491246943

79

This is a large integer,and it's hard to factorize it with usual factorization method,

for example quadratic sieve,but this algorithm can factorize it very fast.

The result of this program:

![](https://github.com/eathimenncvse/SageMath/blob/main/pictures_of_README/6.png)

## Further details of this algorithm

For more details you can read this article
[](https://github.com/eathimenncvse/SageMath/blob/main/Resources/Pollard%20p%20-1%20and%20lenstra.pdf)








