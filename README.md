<h1>Email Separation</h1>
<p>A simple Python program that splits an email address into its username and domain parts.</p>

<h2>Technologies Used</h2>
<ul>
  <li>Python 3</li>
  <li><code>input()</code> and <code>print()</code></li>
  <li>String methods such as <code>find()</code></li>
  <li>String slicing</li>
  <li>Basic conditional statements</li>
</ul>

<h2>Features</h2>
<ul>
  <li>📧 Accepts an email address from the user</li>
  <li>🔍 Checks whether the email contains <code>@</code></li>
  <li>✂️ Extracts the username part before <code>@</code></li>
  <li>🌐 Extracts the domain part after <code>@</code></li>
  <li>⚠️ Shows an error message for invalid email input</li>
</ul>

<h2>Installation</h2>
<ol>
  <li>Make sure Python 3 is installed on your computer.</li>
  <li>Save the script as <code>Email separation.py</code>.</li>
  <li>Open a terminal or command prompt in the same folder.</li>
  <li>Run the program with:</li>
</ol>

<pre><code>python "Email separation.py"</code></pre>

<p>Then enter an email address when prompted.</p>
<p>If the email contains <code>@</code>, the program prints the username and domain separately.</p>
<p>If not, it prints an error message.</p>

<h2>Output</h2>

<h3>Sample Input</h3>
<pre><code>email: user@example.com</code></pre>

<h3>Sample Output</h3>
<pre><code>Username:user
Domain:example.com</code></pre>

<h3>Invalid Input</h3>
<pre><code>email: userexample.com</code></pre>

<h3>Invalid Output</h3>
<pre><code>Your email is incorrect.</code></pre>

<h2>Notes</h2>
<ul>
  <li>⚠️ This script only checks for the presence of <code>@</code>, so it does not fully validate email format.</li>
  <li>💡 It is useful for learning string handling and basic validation in Python.</li>
</ul>
