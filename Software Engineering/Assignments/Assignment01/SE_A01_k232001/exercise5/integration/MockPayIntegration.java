package integration;

import core.PaymentService;
import external.MockPayService;

public class MockPayIntegration implements PaymentService {
    private MockPayService mockService;

    public MockPayIntegration() {
        this.mockService = new MockPayService();
    }

    public boolean pay(double amount) {
        mockService.simulatePayment(amount);
        return true;
    }
}
