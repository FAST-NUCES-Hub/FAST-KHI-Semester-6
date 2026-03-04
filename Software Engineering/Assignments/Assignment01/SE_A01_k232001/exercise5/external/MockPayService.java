package external;

public class MockPayService {
    public void simulatePayment(double amount) {
        System.out.println("[MockPayService] Simulating payment of $" + amount);
        System.out.println("[Test Mode] No real transaction executed.");
    }
}
