package external;

public class LoggingPayService {
    public String processAndConfirm(double amount) {
        return "TXN-OK :: Amount=" + amount;
    }
}
