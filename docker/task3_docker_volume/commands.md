<h2>To create volume</h2>
<code>

    docker run -v /usr/app/node_modules -v $(pwd):/usr/app -p 3000:3000 <image-name>

</code>
