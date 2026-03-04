package integration;

import core.PaymentService;
import external.LoggingPayService;

public class LoggingPayIntegration implements PaymentService {
    private LoggingPayService loggingService;

    public LoggingPayIntegration() {
        this.loggingService = new LoggingPayService();
    }

    public boolean pay(double amount) {
        String confirmation = loggingService.processAndConfirm(amount);
        System.out.println("[AlphaSoft Log] Payment successful -> " + confirmation);
        return true;
    }
}
