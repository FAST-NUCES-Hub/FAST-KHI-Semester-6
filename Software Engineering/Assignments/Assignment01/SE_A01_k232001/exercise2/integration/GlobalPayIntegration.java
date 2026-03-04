package integration;

import core.PaymentService;
import external.GlobalPayService;

public class GlobalPayIntegration implements PaymentService {
    private GlobalPayService globalService;
    private String currency;

    public GlobalPayIntegration(String currency) {
        this.globalService = new GlobalPayService();
        this.currency = currency;
    }

    public boolean pay(double amount) {
        globalService.executeTransaction(currency, amount);
        return true;
    }
}
