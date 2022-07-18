package javaserver;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

import java.io.IOException;
import java.io.OutputStream;

import org.json.simple.JSONObject;
import palindromecheck.PalindromeCounter;

/**
 * Handles the request from frontend
 */
public class MyHttpHandler implements HttpHandler {

    private PalindromeCounter palindromeCounter;

    @Override
    public void handle(HttpExchange httpExchange) throws IOException {

        // Get the query
        String query = httpExchange.getRequestURI().getQuery();

        boolean errorOccured = false;

        // Split query and get variable
        String variable = "";
        String text = "";
        try {
            variable = query.split("=",2)[0];
            text = query.split("=",2)[1];
        } catch (Exception e) {
            errorOccured = true;
            System.out.println("Error with request: " + e);
        }


        ResponseContent responseContent = new ResponseContent();

        // Check if variable correct
        if (variable.contains("text") && !errorOccured) {

            // Pass text to palindrome counter
            palindromeCounter = new PalindromeCounter(text);
            int answer = palindromeCounter.countPalindromes();

            // Build json object with response
            // If string is empty let the user know
            if (answer == -1) {
                responseContent.setError(true);
                responseContent.setString("Error: String empty or Invalid");
                responseContent.setAnswer(0);
            } else {
                responseContent.setError(false);
                responseContent.setString("The answer is " + answer);
                responseContent.setAnswer(answer);
            }
        } else {
            // If variable not in URL, let the user know
            responseContent.setError(false);
            responseContent.setString("Error: Variable \"text\" must be passed to this function");
            responseContent.setAnswer(0);
        }

        // Create JSON Object to return
        JSONObject jsonObject = new JSONObject();

        jsonObject.put("error", responseContent.isError());
        jsonObject.put("string", responseContent.getString());
        jsonObject.put("answer", responseContent.getAnswer());

        // Set response headers
        httpExchange.getResponseHeaders().add("Access-Control-Allow-Origin", "*");
        if (httpExchange.getRequestMethod().equalsIgnoreCase("GET")) {
            httpExchange.getResponseHeaders().add("Access-Control-Allow-Methods", "GET");
            httpExchange.getResponseHeaders().add("Content-type", "application/json");
            if (errorOccured)
                httpExchange.sendResponseHeaders(400, jsonObject.toJSONString().getBytes().length);
            else
                httpExchange.sendResponseHeaders(200, jsonObject.toJSONString().getBytes().length);
        }

        // Write the response
        OutputStream os = httpExchange.getResponseBody();
        os.write(jsonObject.toJSONString().getBytes());

        os.close();
    }
    //https://dzone.com/articles/simple-http-server-in-java
}
