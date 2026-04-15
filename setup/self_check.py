"""
SCM 478 - Self-Check Module
Peak Fuel Foods Supply Chain System

Students select which assignment to check from a dropdown.
Only that assignment's checks are displayed.
"""

import streamlit as st


def _show_result(name, passed, detail, points):
    """Display a single check result with color coding."""
    if passed:
        st.markdown(
            '<div style="background-color: #d4edda; border-left: 4px solid #28a745; '
            'padding: 8px 12px; margin-bottom: 8px; border-radius: 4px;">'
            '<strong style="color: #155724;">PASS</strong> - '
            '<strong>%s</strong> (%d pts)<br/>'
            '<span style="color: #155724;">%s</span></div>'
            % (name, points, detail),
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div style="background-color: #f8d7da; border-left: 4px solid #dc3545; '
            'padding: 8px 12px; margin-bottom: 8px; border-radius: 4px;">'
            '<strong style="color: #721c24;">FAIL</strong> - '
            '<strong>%s</strong> (%d pts)<br/>'
            '<span style="color: #721c24;">%s</span></div>'
            % (name, points, detail),
            unsafe_allow_html=True,
        )


def _discover_assignments():
    """Find all available check modules and collect their assignments."""
    assignments = {}
    unit_modules = [
        "checks.unit1_checks",
        "checks.unit2_checks",
        "checks.unit3_checks",
        "checks.unit4_checks",
    ]

    for module_path in unit_modules:
        try:
            mod = __import__(module_path, fromlist=["get_assignments"])
            if hasattr(mod, "get_assignments"):
                unit_assignments = mod.get_assignments()
                # unit_assignments is a dict: {"Assignment Name": check_function}
                assignments.update(unit_assignments)
        except (ImportError, ModuleNotFoundError):
            pass
        except Exception:
            pass

    return assignments


def run_self_check():
    """Main self-check page. Call this from your app."""

    st.title("Self-Check: Peak Fuel Foods")
    st.caption(
        "Select an assignment below, then check your progress. "
        "Your goal is 100% before submitting."
    )

    # Discover available assignments
    assignments = _discover_assignments()

    if not assignments:
        st.error(
            "No check modules found. Make sure the checks/ folder "
            "is in your repo with __init__.py and at least unit1_checks.py."
        )
        return

    # Let student select which assignment to check
    st.divider()
    assignment_names = list(assignments.keys())
    selected = st.selectbox(
        "Which assignment are you working on?",
        assignment_names,
        index=0,
    )

    st.divider()

    # Run only the selected assignment's checks
    check_fn = assignments[selected]
    try:
        checks = check_fn()
    except Exception as e:
        st.error("Error running checks: %s" % str(e))
        return

    st.header(selected)

    total_earned = 0
    total_possible = 0

    for name, passed, detail, points in checks:
        total_possible += points
        if passed:
            total_earned += points
        _show_result(name, passed, detail, points)

    # Summary
    st.divider()
    pct = int(total_earned / total_possible * 100) if total_possible > 0 else 0

    col1, col2 = st.columns(2)
    col1.metric("Score", "%d%%" % pct)
    col2.metric("Points", "%d / %d" % (total_earned, total_possible))

    if pct == 100:
        st.balloons()
        st.success(
            "All checks passed! This assignment is ready to submit. "
            "Copy your Streamlit URL and submit it on Canvas."
        )
    elif pct >= 75:
        st.warning(
            "%d point(s) remaining. Keep going -- you're almost there."
            % (total_possible - total_earned)
        )
    else:
        st.error(
            "%d point(s) remaining. Fix one issue at a time, commit, "
            "and check again." % (total_possible - total_earned)
        )

    st.divider()
    st.caption(
        "This checker validates data files and app structure. "
        "It cannot verify that filters, charts, and metrics display "
        "correctly -- verify those yourself by clicking through your app."
    )
