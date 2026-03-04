package integration;

import core.PaymentService;
import external.LegacyPayService;

public class LegacyPayIntegration implements PaymentService {
    private LegacyPayService legacyService;

    public LegacyPayIntegration() {
        this.legacyService = new LegacyPayService();
    }

    public boolean pay(double amount) {
        legacyService.makePayment(amount);
        return true;
    }
}
