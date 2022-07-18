package javaserver;

import com.google.gson.Gson;
import com.sun.net.httpserver.HttpServer;
import org.junit.Test;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.InetSocketAddress;
import java.net.URL;
import java.net.URLConnection;

import static org.junit.Assert.assertEquals;

public class MyHttpHandlerTest {

    MyHttpHandler test = new MyHttpHandler();

    @Test
    public void testCallToServer() throws IOException {
        // Create test server
        HttpServer httpServer = HttpServer.create(new InetSocketAddress(8050), 0);
        httpServer.createContext("/", test);
        httpServer.start();

        try {
            // Create request ans send to server
            URL url = new URL("http://localhost:8050/?text=kayak");
            URLConnection conn = url.openConnection();
            BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));

            // Read response
            String jsonString = in.readLine();
            Gson gson = new Gson(); // Or use new GsonBuilder().create();
            ResponseContent content = gson.fromJson(jsonString, ResponseContent.class);

            // Verify response is correct
            assertEquals(1, content.getAnswer());
            assertEquals("The answer is 1", content.getString());
            assertEquals(false, content.isError());
            assertEquals("application/json", conn.getContentType());
        } finally {
            // Stop the server
            httpServer.stop(0);
        }
    }
// https://alistairisrael.wordpress.com/2009/09/02/functional-http-testing-with-sun-java-6-httpserver/
    // https://github.com/google/gson
}