<h1>Flask apps run inside Jython</h1>

python requirements:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*itsdangerous==1.1.0<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*click==7.1.2<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Jinja2==2.11.3<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Werkzeug==1.0.1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*MarkupSafe==1.1.1<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*flask==1.1.4<br>

<br>
java requirements:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*jython-standalone-2.7.3.jar<br>

<h1> When you're running your server, it can run entirely inside jython</h1><br>
One can run the flask server. The exceptions presently are as follows:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*debug mode doesn't work -- "OSError: [Errno 2] No such file or directory" is the error kicked back<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*any port below 5000 doesn't work -- "already in use" is the error kicked back<br>

<h1> What are the advantages of running flask in Jython?</h1><br>

The advantages include:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* flask apps being able to use java classes<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* ability to pass data or class instances (if you know what you're doing)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* gg<br>
