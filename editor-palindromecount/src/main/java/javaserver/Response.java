package javaserver;

public class Response {

    private int answer;
    private String string;
    private boolean error;

    public Response(boolean error, String string, int answer) {
        this.error=error;
        this.string=string;
        this.answer=answer;
    }

    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return "\"Response [error "+ error + ", string = " + string + ", answer = " + answer + "]";
    }

}
