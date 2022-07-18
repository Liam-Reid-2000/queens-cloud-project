using System;
using System.Text;
using System.Net;
using System.Threading.Tasks;

namespace VowelCount
{
    class HttpServer
    {
        public static HttpListener listener;
        public static string url = "http://*:80/";
        //public static string url = "http://localhost:8080/";

        public static async Task HandleIncomingConnections()
        {
            bool runServer = true;

            while (runServer)
            {
                HttpListenerContext ctx = await listener.GetContextAsync();

                HttpListenerRequest req = ctx.Request;
                HttpListenerResponse resp = ctx.Response;

                string textToCheck = req.Url.PathAndQuery;

                // Log for debugging
                if (req.HttpMethod == "GET")
                {
                    Console.WriteLine("GET requested");
                }

                // Get Vowel count
                string answerCount = VowelCounter.CountVowels(textToCheck).ToString();
                // Format JSON response
                string json = "{\"error\":false," +
                  "\"string\":\"There are " + answerCount + " vowels\"," +
                  "\"answer\":" + answerCount + "}";
                // Set headers
                byte[] data = Encoding.UTF8.GetBytes(json);
                resp.Headers.Set("Content-Type", "application/json");
                resp.Headers.Set("Access-Control-Allow-Origin", "*");
                // Encode
                System.Text.Encoding encoding = resp.ContentEncoding;
                if (encoding == null)
                {
                    encoding = System.Text.Encoding.UTF8;
                    resp.ContentEncoding = encoding;
                }
                // Write response
                byte[] buffer = encoding.GetBytes(json);
                resp.ContentLength64 = buffer.Length;
                System.IO.Stream stream = resp.OutputStream;
                stream.Write(buffer, 0, buffer.Length);
                resp.Close();

            }
        }


        public static void Main(string[] args)
        {
            // Create a Http server and start listening for incoming connections
            listener = new HttpListener();
            listener.Prefixes.Add(url);
            listener.Start();
            listener.Start();
            Console.WriteLine("Listening for connections on {0}", url);
            // Handle requests
            Task listenTask = HandleIncomingConnections();
            listenTask.GetAwaiter().GetResult();

            // Close the listener
            listener.Close();
        }
    }
    // https://gist.github.com/define-private-public/d05bc52dd0bed1c4699d49e2737e80e7
}