package client;

import core.PaymentService;
import integration.LegacyPayIntegration;
import integration.GlobalPayIntegration;

public class Main {
    public static void main(String[] args) {
        PaymentService legacy = new LegacyPayIntegration();
        PaymentService global = new GlobalPayIntegration("EUR");

        PaymentClient client = new PaymentClient(legacy);
        client.makePayment(120.0);

        System.out.println("[System] Payment provider switched.");

        client.setService(global);
        client.makePayment(120.0);
    }
}
