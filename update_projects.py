with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find projects section start and end
start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<div class="grid grid-cols-1 md:grid-cols-2 gap-6">' in line and 'id="projects"' in ''.join(lines[max(0, i-10):i]):
        start_idx = i
        break

if start_idx != -1:
    for i in range(start_idx + 1, len(lines)):
        if '</section>' in lines[i]:
            # Backtrack to find the closing div of the grid
            for j in range(i-1, start_idx, -1):
                if '</div>' in lines[j]:
                    end_idx = j
                    break
            break

if start_idx != -1 and end_idx != -1:
    projects_new = """          <!-- 프로젝트 1: UniForum -->
          <div class="project-card bg-surface-container p-6 rounded-xl hover:bg-surface-bright hover:shadow-[0_10px_30px_rgba(19,27,46,0.08)] transition-all duration-300 flex flex-col group border border-outline-variant/10 md:col-span-2">
            <div class="flex justify-between items-start mb-3">
              <div class="flex items-center gap-3">
                <h4 class="font-headline text-xl font-bold text-on-surface group-hover:text-surface-tint transition-colors">UniForum (대학 수업 커뮤니티 웹앱)</h4>
                <span class="text-xs font-label bg-[#4edea3]/20 text-[#005236] dark:text-[#4edea3] px-2 py-0.5 rounded-full font-semibold">캡스톤 디자인 팀 프로젝트 (2025.03 ~ 2025.06)</span>
              </div>
            </div>
            <p class="font-body text-on-surface-variant text-sm mb-4 leading-relaxed">
              수업별 게시판, 질문·답변 기능, 교수 평점 등을 제공하는 학과 커뮤니티 플랫폼. 백엔드 설계 및 API 구현, DB 모델링 담당.<br>
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
              구직자를 위한 정적 포트폴리오 웹사이트 템플릿, 다국어 지원과 Markdown 기반 구조 구현.<br>
              컴포넌트화, CSR/SSR 개념, 타입 안정성을 고려한 설계 방식 익힘.
            </p>
            <div class="flex flex-wrap gap-2 mt-auto">
              <span class="tag">Next.js</span>
              <span class="tag">TypeScript</span>
              <span class="tag">TailwindCSS</span>
            </div>
          </div>
"""
    new_lines = lines[:start_idx + 1] + [projects_new] + lines[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Success")
else:
    print("Failed to find boundaries")
