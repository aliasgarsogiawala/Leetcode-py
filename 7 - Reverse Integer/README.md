<h2><a href="https://leetcode.com/problems/reverse-integer">Reverse Integer</a></h2> 
<img src='https://img.shields.io/badge/Difficulty-Medium-yellow' alt='Difficulty: Medium' />
<hr>
<p>Given a signed 32-bit integer <code>x</code>, return <code>x</code> with its digits reversed. If reversing <code>x</code> causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return <code>0</code>.</p>

<p><strong class="example">Example 1:</strong></p>
<pre>
<strong>Input:</strong> x = 123
<strong>Output:</strong> 321
</pre>

<p><strong class="example">Example 2:</strong></p>
<pre>
<strong>Input:</strong> x = -123
<strong>Output:</strong> -321
</pre>

<p><strong class="example">Example 3:</strong></p>
<pre>
<strong>Input:</strong> x = 120
<strong>Output:</strong> 21
</pre>

<p><strong class="example">Example 4:</strong></p>
<pre>
<strong>Input:</strong> x = 1534236469
<strong>Output:</strong> 0
<strong>Explanation:</strong> The reversed integer overflows 32-bit range.
</pre>

<p><strong>Constraints:</strong></p>
<ul>
	<li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<strong>Approach:</strong>  
Converted the integer to string and reversed it while tracking the sign. After conversion back to int, checked if it's within the 32-bit signed integer range before returning.
