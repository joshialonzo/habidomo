void main(List<String> arguments) {
  int numberOfSections = 6;
  double balanceSection1 = 2500.00;
  double balanceSection2 = 1500.50;
  double balanceSection3 = 3000.75;
  double balanceSection4 = 1200.25;
  double balanceSection5 = 1800.00;
  double balanceSection6 = 2200.00;
  double totalBalance =
      balanceSection1 +
      balanceSection2 +
      balanceSection3 +
      balanceSection4 +
      balanceSection5 +
      balanceSection6;

  String message_1 =
      'Balance of section 1: \$${balanceSection1.toStringAsFixed(2)}';
  String message_2 =
      'Balance of section 2: \$${balanceSection2.toStringAsFixed(2)}';
  String message_3 =
      'Balance of section 3: \$${balanceSection3.toStringAsFixed(2)}';
  String message_4 =
      'Balance of section 4: \$${balanceSection4.toStringAsFixed(2)}';
  String message_5 =
      'Balance of section 5: \$${balanceSection5.toStringAsFixed(2)}';
  String message_6 =
      'Balance of section 6: \$${balanceSection6.toStringAsFixed(2)}';

  print('Number of sections: $numberOfSections');
  print(message_1);
  print(message_2);
  print(message_3);
  print(message_4);
  print(message_5);
  print(message_6);
  print('Total balance: \$${totalBalance.toStringAsFixed(2)}');

  const String name = 'Josué';
  const int age = 30;
  const String city = 'Monterrey';
  String introduction =
      'Hello, my name is $name. I am $age years old and I live in $city.';
  print(introduction);
}
