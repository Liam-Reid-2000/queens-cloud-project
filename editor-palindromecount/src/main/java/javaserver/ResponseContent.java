package javaserver;

/**
 * Simple POJO
 * holds response content to send back to frontend
 */
public class ResponseContent {
    private boolean error;
    private String string;
    private int answer;

    public ResponseContent(boolean error, String string, int answer) {
        this.error = error;
        this.string = string;
        this.answer = answer;
    }

    public ResponseContent() {

    }

    public boolean isError() {
        return error;
    }

    public void setError(boolean error) {
        this.error = error;
    }

    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }

    public int getAnswer() {
        return answer;
    }

    public void setAnswer(int answer) {
        this.answer = answer;
    }
}
