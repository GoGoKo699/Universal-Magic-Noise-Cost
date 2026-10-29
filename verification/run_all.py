"""Run all exact finite checks for the research record."""
import run_checks
import check_full_48

if __name__ == "__main__":
    run_checks.main()
    print("PASS full_48", check_full_48.run())
