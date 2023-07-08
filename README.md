# Python Java Integration

To run the whole project, first run the `main.py` file. By doing that, Python starts listening to incoming socket connections.

Then compile the `JavaClient.java` file, and then run the `JavaClient` to establish a socket connection between Java and Python. They will start to communicate by now.
> You can also directly run `java JavaClient` to start the Java client directly. Note that the `main.py` file should be running and ready for connections.

This way both Java and Python will be able to connect and share information. This will soon be implemented in the [Chess AI in Python](https://github.com/a2ys/chess-ai) to communicate with the [Java Chess Engine](https://github.com/a2ys/java-ai) to take advantage of Java's tremendous speed, and Python's vast support of libraries simultaneously, and create a better AI that could possibly win more games than before!
