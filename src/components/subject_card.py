import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html_parts = []
    html_parts.append('<div style="background: #FFFFFF; border-left: 6px solid #F43F5E; padding: 1.25rem 1.5rem; border-radius: 1.25rem; box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.08); margin-bottom: 0.75rem; border: 1px solid rgba(226, 232, 240, 0.8);">')
    html_parts.append(f'<div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;"><h3 style="margin:0; color: #0F172A; font-size: 1.35rem; font-weight: 700;">{name}</h3><span style="background: #EEF2FF; color: #4F46E5; font-size: 0.85rem; font-weight: 700; padding: 4px 10px; border-radius: 8px; border: 1px solid rgba(79, 70, 229, 0.2);">Code: {code}</span></div>')
    html_parts.append(f'<p style="color: #64748B; margin: 0 0 1rem 0; font-size: 0.95rem; font-weight: 500;">Section: <b style="color: #334155;">{section}</b></p>')

    if stats:
        html_parts.append('<div style="display: flex; gap: 8px; flex-wrap: wrap;">')
        for icon, label, value in stats:
            html_parts.append(f'<div style="background: #FFF1F2; color: #E11D48; padding: 5px 12px; border-radius: 10px; font-size: 0.875rem; font-weight: 600; border: 1px solid rgba(244, 63, 94, 0.2); display: inline-flex; align-items: center; gap: 4px;"><span>{icon}</span> <b>{value}</b> <span style="color: #BE123C;">{label}</span></div>')
        html_parts.append('</div>')

    html_parts.append('</div>')

    st.markdown("".join(html_parts), unsafe_allow_html=True)

    if footer_callback:
        footer_callback()

