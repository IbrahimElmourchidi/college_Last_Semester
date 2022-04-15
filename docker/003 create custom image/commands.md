<h2>To build and image from Dockerfile</h2>
<code>
    
    // . or the path of the docker file
    docker build .

</code>

<h2>To tag an Image</h2>
<code>
    
    // . or the path of the docker file
    docker build -t ibrahimelmourchidi/redis:latest

    // to run the tagged image
    docker run ibrahimelmourchidi/redis

    // if you donot specify version the latest version will be used by default

</code>
