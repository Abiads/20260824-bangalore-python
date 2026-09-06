"""
### Assignment 5: Multi-Channel Notification System (Multiple Inheritance & MRO)
#### Scenario
An automated incident response engine sends server health alert broadcasts. Depending on incident severity, it sends notifications via Email, SMS, or both using cooperative multiple inheritance.

#### Problem Description
Implement a cooperative multiple inheritance structure using the following class designs:
1. **Base Class `Notifier`**:
   - Constructor (`__init__`): Accepts `sender_id` (string).
   - Method `send(message)`: Returns a list containing the log: `["[Notifier <sender_id>] general broadcast: <message>"]`.
2. **Subclass `EmailNotifier` (inherits from `Notifier`)**:
   - Constructor (`__init__`): Accepts `email_server` (string) along with any other keyword parameters. It must forward parameters to the next class in the hierarchy using `super().__init__()` or direct calls.
   - Method `send(message)`: Calls `super().send(message)` to get the log list, prepends the string `"[Email via <email_server>] sending: <message>"` to the list, and returns it.
3. **Subclass `SMSNotifier` (inherits from `Notifier`)**:
   - Constructor (`__init__`): Accepts `sms_gateway` (string) along with any other keyword parameters. It must forward parameters to the next class in the MRO.
   - Method `send(message)`: Calls `super().send(message)` to get the log list, prepends the string `"[SMS via <sms_gateway>] sending: <message>"` to the list, and returns it.
4. **Subclass `HybridAlertChannel` (inherits from BOTH `EmailNotifier` and `SMSNotifier` in that order)**:
   - Constructor (`__init__`): Accepts `sender_id` (string), `email_server` (string), and `sms_gateway` (string). Passes all values cooperatively through `super().__init__()`.
   - Method `send(message)`: Calls `super().send(message)` to get the consolidated log list. Prepends `"[HYBRID ALERT] Initiating dual channels..."` to the list and returns it.
5. **Requirements**:
   - The hierarchy must support **cooperative initialization and cooperative method dispatch**. Calling `super().__init__()` or `super().send()` must pass details down the entire MRO path without skipping parent classes or duplicating calls.
   - Print the Method Resolution Order (`.__mro__` or `.mro()`) of `HybridAlertChannel` to verify the lookup path.

#### Example Walkthrough
```python
alert = HybridAlertChannel(sender_id="SYS-ADMIN", email_server="smtp.cdac.in", sms_gateway="gw.acts.com")
logs = alert.send("Disk space 95%")

for log in logs:
    print(log)
```

**Expected Console Output Logs:**
```text
[HYBRID ALERT] Initiating dual channels...
[Email via smtp.cdac.in] sending: Disk space 95%
[SMS via gw.acts.com] sending: Disk space 95%
[Notifier SYS-ADMIN] general broadcast: Disk space 95%
```
"""

from typing import List


class Notifier:
    def __init__(self, sender_id: str, **kwargs):
        super().__init__(**kwargs)
        self.sender_id = sender_id

    def send(self, message: str) -> List[str]:
        return [f"[Notifier {self.sender_id}] general broadcast: {message}"]


class EmailNotifier(Notifier):
    def __init__(self, email_server: str, **kwargs):
        self.email_server = email_server
        super().__init__(**kwargs)

    def send(self, message: str) -> List[str]:
        logs = super().send(message)
        return [f"[Email via {self.email_server}] sending: {message}"] + logs


class SMSNotifier(Notifier):
    def __init__(self, sms_gateway: str, **kwargs):
        self.sms_gateway = sms_gateway
        super().__init__(**kwargs)

    def send(self, message: str) -> List[str]:
        logs = super().send(message)
        return [f"[SMS via {self.sms_gateway}] sending: {message}"] + logs


class HybridAlertChannel(EmailNotifier, SMSNotifier):
    def __init__(self, sender_id: str, email_server: str, sms_gateway: str, **kwargs):
        super().__init__(
            sender_id=sender_id,
            email_server=email_server,
            sms_gateway=sms_gateway,
            **kwargs,
        )

    def send(self, message: str) -> List[str]:
        logs = super().send(message)
        return ["[HYBRID ALERT] Initiating dual channels..."] + logs


if __name__ == "__main__":
    print("MRO of HybridAlertChannel:")
    for idx, cls in enumerate(HybridAlertChannel.mro()):
        print(f"  {idx + 1}. {cls.__name__}")

    print("\nExecuting HybridAlertChannel.send():")
    alert = HybridAlertChannel(
        sender_id="SYS-ADMIN",
        email_server="smtp.cdac.in",
        sms_gateway="gw.acts.com",
    )
    logs = alert.send("Disk space 95%")

    for log in logs:
        print(log)
