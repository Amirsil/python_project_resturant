
class TestCustomer():

    def setUp(self):
        self.customer = Customer(
            'John Doe', '123-456-7890', 'johndoe@example.com', 'C001')

    def test_place_order_reserved(self):
        order_id = 'O001'
        table_id = 'T001'
        products = ['P001', 'P002']
        total_amount = 100.0
        reservation_status = 'reserved'

        order_mock = Mock()
        order_class_mock = Mock(return_value=order_mock)

        with patch('customer.Order', order_class_mock):
            self.customer.place_order(
                order_id, table_id, products, total_amount, reservation_status)

            order_class_mock.assert_called_once_with(
                order_id, table_id, products, total_amount)
            order_mock.place_order.assert_called_once_with()

        self.assertEqual(self.customer.orders, [order_mock])

    def test_place_order_available(self):
        order_id = 'O002'
        table_id = 'T002'
        products = ['P003']
        total_amount = 50.0
        reservation_status = 'available'

        order_mock = Mock()
        order_class_mock = Mock(return_value=order_mock)

        with patch('customer.Order', order_class_mock):
            self.customer.place_order(
                order_id, table_id, products, total_amount, reservation_status)

            order_class_mock.assert_called_once_with(
                order_id, table_id, products, total_amount)
            order_mock.place_order.assert_called_once_with()

        self.assertEqual(self.customer.orders, [order_mock])

    def test_place_order_invalid_reservation_status(self):
        order_id = 'O003'
        table_id = 'T003'
        products = ['P004', 'P005']
        total_amount = 75.0
        reservation_status = 'invalid'

        order_class_mock = Mock()

        with patch('customer.Order', order_class_mock):
            self.customer.place_order(
                order_id, table_id, products, total_amount, reservation_status)

            order_class_mock.assert_not_called()

        self.assertEqual(self.customer.orders, [])
