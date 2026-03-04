package external;

public class LegacyPayService {
    public void makePayment(double valueInDollars) {
        System.out.println("[LegacyPayService] Processing payment of $" + valueInDollars);
    }
}
