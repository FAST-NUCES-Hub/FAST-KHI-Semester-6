package external;

public class GlobalPayService {
    public void executeTransaction(String currency, double value) {
        System.out.println("[GlobalPayService] Processing " + value + " " + currency);
    }
}
