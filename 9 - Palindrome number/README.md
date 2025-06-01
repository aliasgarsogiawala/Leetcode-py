<h2><a href="https://leetcode.com/problems/palindrome-number">Palindrome Number</a></h2>  
<img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />  
<hr>  
<p>Given an integer <code>x</code>, return <code>true</code> if <code>x</code> is a palindrome integer.</p>

<p>An integer is a palindrome when it reads the same backward as forward. For example, <code>121</code> is a palindrome while <code>123</code> is not.</p>

<p><strong class="example">Example 1:</strong></p>  
<pre>
<strong>Input:</strong> x = 121
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>  
<pre>
<strong>Input:</strong> x = -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>  
<pre>
<strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

<p><strong>Constraints:</strong></p>  
<ul>  
  <li><code>-2<sup>31</sup> &lt;= x &lt;= 2<sup>31</sup> - 1</code></li>  
</ul>

<strong>Approach:</strong>  
Converted the integer to string, then compared it to its reverse. Negative numbers automatically return false due to the '-' sign.
