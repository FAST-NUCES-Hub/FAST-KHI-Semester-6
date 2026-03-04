package client;

import core.PaymentService;
import integration.LegacyPayIntegration;

public class Main {
    public static void main(String[] args) {
        PaymentService service = new LegacyPayIntegration();
        PaymentClient client = new PaymentClient(service);
        client.makePayment(250.0);
    }
}
