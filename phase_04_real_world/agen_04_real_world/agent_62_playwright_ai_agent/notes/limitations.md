# Limitations: Playwright AI Agent

This agent does NOT:

- Perform visual regression testing or pixel-level screenshot comparison
- Execute tests across multiple browsers in parallel — single browser per invocation
- Handle multi-factor authentication, CAPTCHA, or biometric challenges
- Re-analyze the page mid-test when the DOM changes after an action (single snapshot at start)
- Support native mobile app testing — web browser only
- Integrate with pytest or any test framework natively — standalone invocation
- Guarantee LLM-generated locators will work on first try for highly dynamic apps (React/Angular with server-side IDs)
- Take screenshots at every step — only on failure
- Manage test data setup or teardown (database seeding, account creation)
- Handle iframes, shadow DOM, or file upload dialogs without explicit caller guidance
