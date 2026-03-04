package integration;

import core.PaymentService;
import external.CentPayService;

public class CentPayIntegration implements PaymentService {
    private CentPayService centService;

    public CentPayIntegration() {
        this.centService = new CentPayService();
    }

    public boolean pay(double amount) {
        int cents = (int) (amount * 100);
        centService.processInCents(cents);
        return true;
    }
}
