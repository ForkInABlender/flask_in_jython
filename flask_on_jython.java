import org.python.util.PythonInterpreter;

public class flask_on_jython{
  public static void main(String[] args) {
    PythonInterpreter py = new PythonInterpreter();
    py.execfile("flask_test.py");
  }
}
