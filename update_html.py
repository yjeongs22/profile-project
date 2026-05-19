import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Social Links
html = html.replace('https://github.com/yeonjeong-choi', 'https://github.com/yjeongs22')
html = html.replace('https://linkedin.com/in/yeonjeong-choi', 'https://linkedin.com/in/juhyun-dev')

# 2. Update Skills in Sidebar
skills_new = '''          <h3 class="font-headline font-bold text-surface-tint mb-3 text-xs uppercase tracking-widest">Languages</h3>
          <div class="flex flex-wrap gap-2 mb-5">
            <span class="skill-tag"><span class="w-1.5 h-1.5 rounded-full bg-tertiary-fixed-dim inline-block"></span> JavaScript</span>
            <span class="skill-tag"><span class="w-1.5 h-1.5 rounded-full bg-tertiary-fixed-dim inline-block"></span> TypeScript</span>
            <span class="skill-tag"><span class="w-1.5 h-1.5 rounded-full bg-tertiary-fixed-dim inline-block"></span> Python</span>
          </div>

          <h3 class="font-headline font-bold text-surface-tint mb-3 text-xs uppercase tracking-widest">Frameworks</h3>
          <div class="flex flex-wrap gap-2 mb-5">
            <span class="skill-tag"><span class="w-1.5 h-1.5 rounded-full bg-tertiary-fixed-dim inline-block"></span> Node.js</span>
            <span class="skill-tag"><span class="w-1.5 h-1.5 rounded-full bg-tertiary-fixed-dim inline-block"></span> Express</span>
            <span class="skill-tag"><span class="w-1.5 h-1.5 rounded-full bg-tertiary-fixed-dim inline-block"></span> Next.js</span>
            <span class="skill-tag"><span class="w-1.5 h-1.5 rounded-full bg-tertiary-fixed-dim inline-block"></span> React</span>
          </div>

          <h3 class="font-headline font-bold text-surface-tint mb-3 text-xs uppercase tracking-widest">Database & Tools</h3>
          <div class="flex flex-wrap gap-2 mb-6">
            <span class="skill-tag"><span class="w-1.5 h-1.5 rounded-full bg-tertiary-fixed-dim inline-block"></span> MySQL</span>
            <span class="skill-tag"><span class="w-1.5 h-1.5 rounded-full bg-tertiary-fixed-dim inline-block"></span> MongoDB</span>
            <span class="skill-tag"><span class="w-1.5 h-1.5 rounded-full bg-tertiary-fixed-dim inline-block"></span> Git/GitHub</span>
            <span class="skill-tag"><span class="w-1.5 h-1.5 rounded-full bg-tertiary-fixed-dim inline-block"></span> Postman</span>
            <span class="skill-tag"><span class="w-1.5 h-1.5 rounded-full bg-tertiary-fixed-dim inline-block"></span> Figma</span>
            <span class="skill-tag"><span class="w-1.5 h-1.5 rounded-full bg-tertiary-fixed-dim inline-block"></span> Docker(기초)</span>
          </div>'''
html = re.sub(r'<h3 class=\"font-headline font-bold text-surface-tint mb-3 text-xs uppercase tracking-widest\">Languages</h3>.*?<a href=\"mailto:', skills_new + '\n\n          <a href=\"mailto:', html, flags=re.DOTALL)

# 3. Update Hero Section
hero_new = '''          <h2
            class="font-headline text-4xl md:text-5xl font-extrabold text-on-surface tracking-tighter mb-6 leading-tight">
            꾸준한 학습과 실습을 통해
            <span class="bg-clip-text text-transparent bg-gradient-to-r from-[#124af0] to-[#4edea3]">
              실무 역량을 갖춘
            </span>
            신입 백엔드 개발자입니다.
          </h2>
          <div class="font-body text-on-surface-variant text-lg max-w-3xl leading-relaxed space-y-4">
            <p>저는 꾸준히 학습하고, 실습으로 검증해온 준비된 개발 인재 최연정입니다.</p>
            <p>배재대학교 게임공학과 재학 중 다양한 프로젝트를 통해 백엔드 개발과 데이터 흐름에 깊은 흥미를 느꼈고, 실용적인 코드를 지향하며 문제 해결 능력을 키워왔습니다.</p>
            <p>Node.js와 MySQL을 기반으로 한 API 서버 구축 경험이 있으며, 팀 프로젝트에서는 기획자와 소통하며 요구사항을 기술로 구현하는 과정에 강점을 보였습니다.</p>
            <p>졸업을 앞두고 백엔드 개발자로서 <strong class="text-on-surface font-semibold">문제를 스스로 정의하고 해결할 줄 아는 개발자</strong>가 되기 위해 노력하고 있습니다.</p>
          </div>'''
html = re.sub(r'<h2\s+class=\"font-headline text-4xl md:text-6xl.*?</p>', hero_new, html, flags=re.DOTALL)

# 4. Hide old Activities
html = html.replace('<section id="experience">', '<section id="experience" class="hidden">')

# 5. Update Projects
projects_new = '''          <!-- 프로젝트 1: UniForum -->
          <div class="project-card bg-surface-container p-6 rounded-xl hover:bg-surface-bright hover:shadow-[0_10px_30px_rgba(19,27,46,0.08)] transition-all duration-300 flex flex-col group border border-outline-variant/10 md:col-span-2">
            <div class="flex justify-between items-start mb-3">
              <div class="flex items-center gap-3">
                <h4 class="font-headline text-xl font-bold text-on-surface group-hover:text-surface-tint transition-colors">UniForum (대학 수업 커뮤니티 웹앱)</h4>
                <span class="text-xs font-label bg-[#4edea3]/20 text-[#005236] dark:text-[#4edea3] px-2 py-0.5 rounded-full font-semibold">캡스톤 디자인 팀 프로젝트 (2025.03 ~ 2025.06)</span>
              </div>
            </div>
            <p class="font-body text-on-surface-variant text-sm mb-4 leading-relaxed">
              수업별 게시판, 질문·답변 기능, 교수 평점 등을 제공하는 학과 커뮤니티 플랫폼. 백엔드 설계 및 API 구현, DB 모델링 담당.
              기획~배포까지 전 과정을 직접 경험, 백엔드 안정성과 유지보수성에 대한 감각을 익힘.
            </p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="tag">Node.js</span>
              <span class="tag">Express</span>
              <span class="tag">MySQL</span>
              <span class="tag">Bootstrap</span>
            </div>
          </div>

          <!-- 프로젝트 2: DevResume -->
          <div class="project-card bg-surface-container p-6 rounded-xl hover:bg-surface-bright hover:shadow-[0_10px_30px_rgba(19,27,46,0.08)] transition-all duration-300 flex flex-col group border border-outline-variant/10 md:col-span-2">
            <div class="flex justify-between items-start mb-3">
              <div class="flex items-center gap-3">
                <h4 class="font-headline text-xl font-bold text-on-surface group-hover:text-surface-tint transition-colors">DevResume (개발자 포트폴리오 템플릿)</h4>
                <span class="text-xs font-label bg-[#4edea3]/20 text-[#005236] dark:text-[#4edea3] px-2 py-0.5 rounded-full font-semibold">개인 프로젝트 (2024.01 ~ 2024.02)</span>
              </div>
            </div>
            <p class="font-body text-on-surface-variant text-sm mb-4 leading-relaxed">
              구직자를 위한 정적 포트폴리오 웹사이트 템플릿, 다국어 지원과 Markdown 기반 구조 구현.
              컴포넌트화, CSR/SSR 개념, 타입 안정성을 고려한 설계 방식 익힘.
            </p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="tag">Next.js</span>
              <span class="tag">TypeScript</span>
              <span class="tag">TailwindCSS</span>
            </div>
          </div>'''
html = re.sub(r'<div class=\"grid grid-cols-1 md:grid-cols-2 gap-6\">.*?<!-- ── Certifications & Education ── -->', '<div class="grid grid-cols-1 md:grid-cols-2 gap-6">\n' + projects_new + '\n        </div>\n      </section>\n\n      <!-- ── Certifications & Education ── -->', html, flags=re.DOTALL)

# 6. Update Certs & Education
certs_edu_new = '''          <!-- 자격증 -->
          <div
            class="flex items-center gap-4 p-4 bg-surface-container-lowest rounded-xl border border-outline-variant/20 hover:border-surface-tint/30 transition-all">
            <span class="material-symbols-outlined text-surface-tint text-3xl shrink-0">verified</span>
            <div>
              <div class="font-headline font-bold text-on-surface text-sm">정보처리기능사</div>
              <div class="font-label text-xs text-on-surface-variant mt-0.5">한국산업인력공단 · 2023.11 취득</div>
            </div>
          </div>
          <div
            class="flex items-center gap-4 p-4 bg-surface-container-lowest rounded-xl border border-outline-variant/20 hover:border-surface-tint/30 transition-all">
            <span class="material-symbols-outlined text-surface-tint text-3xl shrink-0">verified</span>
            <div>
              <div class="font-headline font-bold text-on-surface text-sm">SQLD (SQL 개발자)</div>
              <div class="font-label text-xs text-on-surface-variant mt-0.5">한국데이터산업진흥원 · 2024.02 취득</div>
            </div>
          </div>
          <div
            class="flex items-center gap-4 p-4 bg-surface-container-lowest rounded-xl border border-outline-variant/20 hover:border-surface-tint/30 transition-all">
            <span class="material-symbols-outlined text-surface-tint text-3xl shrink-0">verified</span>
            <div>
              <div class="font-headline font-bold text-on-surface text-sm">컴퓨터활용능력 1급</div>
              <div class="font-label text-xs text-on-surface-variant mt-0.5">대한상공회의소 · 2022.12 취득</div>
            </div>
          </div>

          <!-- 학력 -->
          <div
            class="md:col-span-2 flex items-center gap-4 p-4 bg-surface-container-lowest rounded-xl border border-outline-variant/20 hover:border-surface-tint/30 transition-all">
            <span class="material-symbols-outlined text-surface-tint text-3xl shrink-0">school</span>
            <div class="flex-1">
              <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1">
                <div class="font-headline font-bold text-on-surface text-sm">배재대학교 게임공학과</div>
              </div>
              <div class="font-label text-xs text-on-surface-variant mt-0.5">2023.03 ~ 2027.02 (예정) · 주요 수강과목: 웹프로그래밍, 데이터베이스, 알고리즘</div>
            </div>
          </div>'''
html = re.sub(r'<!-- 자격증 -->.*?</div>\n      </section>', certs_edu_new + '\n        </div>\n      </section>', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
