package client;

import core.PaymentService;
import integration.GlobalPayIntegration;

public class Main {
    public static void main(String[] args) {
        PaymentService service = new GlobalPayIntegration("USD");
        PaymentClient client = new PaymentClient(service);
        client.makePayment(150.75);
    }
}
