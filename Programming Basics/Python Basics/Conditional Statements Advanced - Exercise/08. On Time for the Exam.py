def get_diff_in_min(h1, m1, h2, m2):
    if m1 < m2:
        h1 -= 1
        m1 += 60
    if m1 == 0 and m2 != 0:
        m1 = 60
    h_diff = h2 - h1
    m_diff = m2 - m1

    return h_diff * 60 + m_diff


def convert_min_to_h_min_message(minutes):
    if abs(minutes) < 60:
        h = 0
    else:
        h = abs(minutes) // 60
    m = abs(minutes) % 60

    before_or_after = "after"
    if minutes < 0:
        before_or_after = "before"

    if minutes == 0:
        return ""

    if h == 0:
        if m == 0:
            return f"{abs(m):02} minutes {before_or_after} the start"
        return f"{abs(m)} minutes {before_or_after} the start"
    else:
        return f"{abs(h)} {m:02} hours {before_or_after} the start"


h_exam = int(input())
m_exam = int(input())

h_arrival = int(input())
m_arrival = int(input())

minutes_diff = get_diff_in_min(h_exam, m_exam, h_arrival, m_arrival)

if -30 <= minutes_diff <= 0:
    print(f"On time {convert_min_to_h_min_message(minutes_diff)}")
elif minutes_diff < -30:
    print(f"Early {convert_min_to_h_min_message(minutes_diff)}")
elif minutes_diff > 0:
    print(f"Late {convert_min_to_h_min_message(minutes_diff)}")

